"""
    メニュー関連
"""
import os
from django.contrib import messages
from django.contrib.messages import get_messages
from django.core.mail import send_mail
from django.db.models import Prefetch
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import generic
from recipe.core.models import Cuisine, Instruction


class CuisineListView(generic.ListView):
    """ 料理一覧 """
    model = Cuisine
    template_name = 'cuisine.dhtml'

    def __init__(self):
        self.title = '料理一覧'

    def get(self, request: HttpRequest, *args, **kwargs):
        out_messages = [msg for msg in get_messages(request)]

        return render(request, self.template_name, {
            'title': self.title,
            'message': '' if not out_messages else out_messages[0],
        })


def notice(request: HttpRequest, pk: int):
    """
    メール送信
    @param request
    @param pk
    @return: redirect
    """
    prefetch = Prefetch(
        'instructions', queryset=Instruction.objects.order_by('sort_order'))
    cuisine = Cuisine.objects.prefetch_related(
        prefetch, 'foodstuffs').get(pk=pk)

    mail_body = get_template('_partial/email.dhtml').render({
        'name': cuisine.name,
        'instructions': cuisine.instructions.all(),
        'foodstuffs': cuisine.foodstuffs.all(),
    })

    send_mail('レシピ通知【%s】' % cuisine.name, mail_body,
              os.environ.get('EMAIL_HOST_USER'), [request.user.mail_address])

    messages.add_message(request, messages.INFO,
                         '【%s】のレシピをメール送信しました。' % cuisine.name)
    return redirect('recipe_cuisine:index')
