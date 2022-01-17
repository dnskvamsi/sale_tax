from django.db import models

# Create your models here.
class ItemDetalis(models.Model):
    quantity = models.IntegerField()
    item_description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=3, decimal_places=2)
