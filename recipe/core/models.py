# pylint: disable=C0103
""" Models """
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """ API認証ユーザ """
    REQUIRED_FIELDS = ['email']

    access_token = None
    name = None

    def get_access_token(self):
        """ アクセストークン取得 """
        return self.access_token if hasattr(self, 'access_token') else None

    def get_full_name(self):
        if self.name:
            return self.self.name

        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    @property
    def is_authenticated(self):
        return True if self.get_username() else False

    def from_json(self, data):
        """ JSONの値をオブジェクトに設定 """
        self.pk = data.get('id')
        self.access_token = data.get('accessToken')
        self.username = data.get('account')
        self.name = data.get('name')
        self.email = data.get('mailAddress')
        if data.get('admin'):
            self.is_superuser = data.get('admin')
        elif data.get('role'):
            self.is_superuser = True if data.get('role') == '管理者' else False
        return self

    def to_json(self):
        """ オブジェクトの値をJSONで取得 """
        return {
            'id': self.pk,
            'accessToken': self.get_access_token(),
            'account': self.get_username(),
            'name': self.get_full_name(),
            'mailAddress': self.email,
            'admin': self.is_superuser,
        }

    class Meta(AbstractUser.Meta):
        app_label = 'core'
        db_table = 'auth_user'
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'
        abstract = False


class BaseModel(models.Model):
    """ 基底モデル """

    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    modified_by = models.CharField(max_length=10)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.pk is None:
            self.created = timezone.now()

        self.modified = timezone.now()

        # 親の処理を呼び出し
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True


class Cuisine(BaseModel):
    """ メニュー """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=20)
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
    cuisine = models.ForeignKey(
        Cuisine, models.CASCADE, related_name='instructions')

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
    cuisine = models.ForeignKey(
        Cuisine, models.CASCADE, related_name='foodstuffs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstuffs'
        verbose_name = '食材'
        verbose_name_plural = '食材'
