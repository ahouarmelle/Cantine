from django import forms
from menu.models.menu_model import MenuModel


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = ['plat', 'creation_date',]
        widgets = {
            'creation_date': forms.DateInput(attrs={'type':'date'}),
        }