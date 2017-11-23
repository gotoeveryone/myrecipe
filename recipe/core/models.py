""" Models """
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class MyUser(User):
    """ API認証に成功したユーザモデル """
    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'mail_address'
    REQUIRED_FIELDS = ['id', 'user_id', 'user_name', 'mail_address', 'role']

    authenticated = False

    def __init__(self, access_token, user_info, *args, **kwargs):
        super(MyUser, self).__init__(*args, **kwargs)
        self.pk = user_info.get('id')
        self.user_id = user_info.get('account')
        self.user_name = user_info.get('name')
        self.sex = user_info.get('sex')
        self.mail_address = user_info.get('mailAddress')
        self.access_token = access_token

        # ユーザの権限設定
        self.is_active = True
        self.is_staff = True
        self.is_superuser = True if user_info.get('role') == '管理者' else False

        # 認証済み
        self.authenticated = True

    def get_access_token(self):
        return self.access_token

    def get_full_name(self):
        return self.get_short_name()

    def get_short_name(self):
        return self.user_name

    def is_authenticated(self):
        return self.authenticated

    def save(self, *args, **kwargs):
        pass

    class Meta:
        verbose_name = 'ログインユーザ'
        verbose_name_plural = 'ログインユーザ'
        managed = False


class BaseModel(models.Model):
    """ 基底モデル """

    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    modified_by = models.CharField(max_length=10)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.id is None:
            self.created = timezone.now()

        self.modified = timezone.now()

        # 親の処理を呼び出し
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Cuisine(BaseModel):
    """ メニュー """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)
    ingestion_kcal = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(9999)])
    create_number_of_times = models.IntegerField(
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(999)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cuisine'
        verbose_name = 'メニュー'
        verbose_name_plural = 'メニュー'


class Instruction(BaseModel):
    """ 調理手順 """
    sort_order = models.IntegerField('並び順',
                                     validators=[MinValueValidator(1), MaxValueValidator(999)])
    description = models.CharField('手順', max_length=255)
    cuisine = models.ForeignKey(Cuisine, related_name='instructions')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cooking_instructions'
        verbose_name = '調理手順'
        verbose_name_plural = '調理手順'


class Foodstuff(BaseModel):
    """ 食材 """
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, related_name='foodstuffs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstuffs'
        verbose_name = '食材'
        verbose_name_plural = '食材'
