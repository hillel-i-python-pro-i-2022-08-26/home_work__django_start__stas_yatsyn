from django.urls import path

from . import views

urlpatterns = [
    path('create/<name>', views.create, name="index"),
    path('', views.index, name="index"),
]

