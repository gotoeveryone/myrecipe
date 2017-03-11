""" Models """
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cuisine(models.Model):
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

class Instruction(models.Model):
    """ 調理手順 """
    sort_order = models.IntegerField('並び順',\
        validators=[MinValueValidator(1), MaxValueValidator(3)])
    description = models.CharField('手順', max_length=255)
    cuisine = models.ForeignKey(Cuisine, related_name='instructions')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'cooking_instructions'

class Foodstuff(models.Model):
    """ 食材 """
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'foodstuffs'

class Quantity(models.Model):
    """ 数量 """
    detail = models.CharField(max_length=100)
    cuisine = models.ForeignKey(Cuisine, related_name='quantities')
    foodstuff = models.OneToOneField(Foodstuff, related_name='foodstuff')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'quantities'
