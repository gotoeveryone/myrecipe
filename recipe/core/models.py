""" Models """
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class BaseModel(models.Model):
    """ 基底モデル """

    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.CharField(null=True, max_length=10)
    modified_by = models.CharField(null=True, max_length=10)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.id is None:
            self.created = timezone.now()

        self.modified = timezone.now()

        # 親の処理を呼び出し
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

class MyUser(AbstractBaseUser):
    """
    API認証を行うためのユーザモデル
    """
    USERNAME_FIELD = 'user_name'
    EMAIL_FIELD = 'mail_address'
    REQUIRED_FIELDS = ['user_id', 'user_name', 'mail_address', 'role']

    user_id = models.CharField(max_length=16)
    user_name = models.CharField(max_length=32)
    sex = models.CharField(max_length=2)
    email_address = models.CharField(max_length=50)
    role = models.CharField(max_length=3)
    token = models.CharField(max_length=50)

    def __init__(self, token, user_info, *args, **kwargs):
        super(MyUser, self).__init__(*args, **kwargs)
        self.id = user_info.get('id')
        self.user_id = user_info.get('userId')
        self.user_name = user_info.get('userName')
        self.sex = user_info.get('sex')
        self.email_address = user_info.get('mailAddress')
        self.sub_mail_address = user_info.get('subMailAddress')
        self.role = user_info.get('role')
        self.is_active = user_info.get('active')
        self.token = token

    def save(self, *args, **kwargs):
        pass

class Cuisine(BaseModel):
    """ メニュー """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)
    ingestion_kcal = models.IntegerField(\
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(9999)])
    create_number_of_times = models.IntegerField(\
        blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(999)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cuisine'

class Instruction(BaseModel):
    """ 調理手順 """
    sort_order = models.IntegerField('並び順',\
        validators=[MinValueValidator(1), MaxValueValidator(999)])
    description = models.CharField('手順', max_length=255)
    cuisine = models.ForeignKey(Cuisine, related_name='instructions')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cooking_instructions'

class Foodstuff(BaseModel):
    """ 食材 """
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, related_name='foodstuffs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstuffs'
