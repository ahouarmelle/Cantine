from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel

# Create your models here.

class PlatModel(NamedDateTimeModel):

    summary = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"

    def __str__(self):
        return f"{self.name}"