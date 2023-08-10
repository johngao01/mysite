from django.urls import path

from . import views

urlpatterns = [
    path("", views.item_list, name="index"),
    path("show", views.item_show, name="show    "),
]
