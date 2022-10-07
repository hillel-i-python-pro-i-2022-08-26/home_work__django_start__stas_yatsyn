from django.urls import path

from . import views

urlpatterns = [
    path("<name>", views.index, name="input_data"),
    path("", views.index, name="index"),
]

