from django.urls import path
from curso_django.courses import views

urlpatterns = [
    path('', views.index, name='index'),
]
