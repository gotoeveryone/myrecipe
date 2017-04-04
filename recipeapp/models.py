""" Models """
import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BaseModel(models.Model):
    """ 基底モデル """

    created = models.DateTimeField()
    modified = models.DateTimeField()
    created_by = models.CharField(max_length=10)
    modified_by = models.CharField(max_length=10)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id is None:
            self.created = datetime.datetime.now()

        self.modified = datetime.datetime.now()

        # 親の処理を呼び出し
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

class Cuisine(BaseModel):
    """ メニュー """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)
    ingestion_kcal = models.IntegerField(\
        validators=[MinValueValidator(1), MaxValueValidator(9999)])
    create_number_of_times = models.IntegerField(\
        validators=[MinValueValidator(1), MaxValueValidator(999)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cuisine'

class Instruction(BaseModel):
    """ 調理手順 """
    sort_order = models.IntegerField('並び順',\
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = models.CharField('手順', max_length=255)
    cuisine = models.ForeignKey(Cuisine, related_name='instructions')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cooking_instructions'

class Foodstuff(BaseModel):
    """ 食材 """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstuffs'

class Quantity(BaseModel):
    """ 数量 """
    detail = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, related_name='quantities')
    foodstuff = models.OneToOneField(Foodstuff, related_name='foodstuff')

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'quantities'
