from django import forms
from plat.models.plat_model import PlatModel


class PlatForm(forms.ModelForm):
    class Meta:
        model = PlatModel
        fields = ['name', 'summary',]
        