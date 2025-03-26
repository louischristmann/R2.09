from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
]

urlpatterns2 = [
    path('formulaire/', views.index),
]