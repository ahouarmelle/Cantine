from django.urls import path
from .views import index,add, update, delete 




app_name="menu"
urlpatterns = [
    path('', index,name="index"),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-menu"),
    path('delete/<int:id>',delete,name="delete-menu"),
]