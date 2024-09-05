from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.

class MenuModel(DateTimeModel):
    plat = models.OneToOneField('plat.PlatModel', on_delete=models.CASCADE)
    creation_date = models.DateTimeField()

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f"{self.plat},{self.created_at}"