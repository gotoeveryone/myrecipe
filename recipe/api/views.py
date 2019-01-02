""" APIのビューセット """
from logging import getLogger
from django.conf import settings
from django.contrib import auth
from django.core.mail import send_mail
from django.db.models import Prefetch
from django.template.loader import get_template
from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from recipe.api.handler import response401
from recipe.api.serializer import CuisineSerializer, CuisineListSerializer, ClassificationSerializer, FoodstuffListSerializer
from recipe.core.forms import LoginForm
from recipe.core.models import UserToken, Cuisine, Classification, Foodstuff, Instruction


def required_token_decorator(dispatch):
    """ トークン必須チェック """

    def wrapper(request: Request, *args, **kwargs):
        logger = getLogger(__name__)

        # リクエストヘッダ取得
        token_string = request.META.get('HTTP_AUTHORIZATION')
        if not token_string:
            # Apacheだとデフォルトで環境変数にAuthorizationが追加されないため、.htaccessで追加する必要がある
            # 上記で設定した場合は環境変数名が`REDIRECT_HTTP_AUTHORIZATION`となるため、その値も参照する
            token_string = request.META.get('REDIRECT_HTTP_AUTHORIZATION')
            if not token_string:
                logger.info('認証エラー（Authorization ヘッダが存在しない）')
                return response401()

        # トークン文字列を取得
        token = token_string.replace('Bearer ', '')
        if not token:
            logger.info('認証エラー（Authorization ヘッダにトークンが存在しない）')
            return response401()

        user_token = UserToken.objects.filter(
            token=token, expired__gte=timezone.now()).order_by('-expired').first()
        if not user_token:
            logger.info('認証エラー（トークンが不正）')
            return response401()

        request.user = user_token.user
        return dispatch(request, *args, **kwargs)

    return wrapper


@method_decorator(required_token_decorator, name='dispatch')
class CuisineViewSet(viewsets.ModelViewSet):
    """ メニュー REST API """
    queryset = Cuisine.objects
    serializer_class = CuisineSerializer
    user = None

    def list(self, request: Request, *args, **kwargs):
        self.serializer_class = CuisineListSerializer
        return super(CuisineViewSet, self).list(self, request, *args, **kwargs)

    def create(self, request: Request, *args, **kwargs):
        # 登録ユーザの追加
        request.data['created_by'] = request.user.username
        request.data['modified_by'] = request.user.username
        return super(CuisineViewSet, self).create(request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs):
        # 更新ユーザの追加
        request.data['modified_by'] = request.user.username
        return super(CuisineViewSet, self).update(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name)

        classification = self.request.query_params.get('classification')
        if classification:
            queryset = queryset.filter(classification=classification)

        kcal = self.request.query_params.get('kcal')
        if kcal:
            queryset = queryset.filter(ingestion_kcal__lte=kcal)

        return queryset


@method_decorator(required_token_decorator, name='dispatch')
class ClassificationViewSet(viewsets.ModelViewSet):
    """ 調理分類 REST API """
    queryset = Classification.objects.order_by('sort_order')
    serializer_class = ClassificationSerializer


@method_decorator(required_token_decorator, name='dispatch')
class FoodstuffViewSet(viewsets.ModelViewSet):
    """ 食材 REST API """
    queryset = Foodstuff.objects.distinct().order_by('name').values('name')
    serializer_class = FoodstuffListSerializer


@api_view()
def health(request: Request):
    """ 死活監視 """
    return Response({
        'message': 'OK',
    }, status=status.HTTP_200_OK)


@api_view(http_method_names=('post',))
def login(request: Request, *args, **kwargs):
    """ ログイン """
    form = LoginForm(request.data)
    if not form.is_valid():
        return Response({
            'code': status.HTTP_400_BAD_REQUEST,
            'message': form.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    user = auth.authenticate(request,
                             username=form.cleaned_data['account'],
                             password=form.cleaned_data['password'])

    if user is None:
        return response401()

    user_token = UserToken.objects.create(
        token=user.generate_access_token(),
        expired=timezone.now() + timezone.timedelta(minutes=10),
        user=user,
    )

    return Response({
        'token': user_token.token,
    }, status=status.HTTP_200_OK)


@api_view(http_method_names=('delete',))
def logout(request: Request, *args, **kwargs):
    """ ログアウト """
    if request.user.is_authenticated:
        UserToken.objects.filter(
            token=request.user.user_token,
        ).delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


@required_token_decorator
@api_view()
def user(request: Request, *args, **kwargs):
    """ ユーザ情報返却 """
    return Response(request.user.to_json(), status=status.HTTP_200_OK)


@required_token_decorator
@api_view(http_method_names=('post',))
def notice(request: Request, *args, **kwargs):
    """ メール送信 """
    prefetch = Prefetch(
        'instructions', queryset=Instruction.objects.order_by('sort_order'))
    cuisine = Cuisine.objects.prefetch_related(
        prefetch, 'foodstuffs').get(pk=request.data['id'])

    mail_body = get_template('_partial/email.dhtml').render({
        'name': cuisine.name,
        'instructions': cuisine.instructions.all(),
        'foodstuffs': cuisine.foodstuffs.all(),
    })

    from_email = '%s <%s>' % (
        settings.EMAIL_FROM_ALIAS, settings.EMAIL_FROM_USER)
    send_mail('レシピ通知【%s】' % cuisine.name, mail_body,
              from_email, [request.user.email])

    return Response({
        'message': 'OK',
    }, status=status.HTTP_200_OK)
