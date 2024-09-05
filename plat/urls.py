from django.urls import path
from .views import index,add, update, delete 




app_name="plat"
urlpatterns = [
    path('', index,name="index"),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-plat"),
    path('delete/<int:id>',delete,name="delete-plat"),
]