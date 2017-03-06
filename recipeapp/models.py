from django.db import models

class Foodstuff(models.Model):
    name = models.CharField(max_length=255)
    classification = models.CharField(max_length=5)

    def __str__(self):
            return self.name

    class Meta:
        db_table = 'foodstuffs'
    