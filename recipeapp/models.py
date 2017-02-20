from django.db import models

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)
    ingestion_kcal = models.IntegerField(max_length=4)
    create_number_of_times = models.IntegerField(max_length=3)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'cuisine'

class Foodstuff(models.Model):
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'foodstuffs'
    