from django.urls import path
from curso_django.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]
