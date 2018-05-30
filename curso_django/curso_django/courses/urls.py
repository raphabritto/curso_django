from django.urls import path, include
from curso_django.courses import views

urlpatterns = [
    path('', include('views.index'), name='index'),
]
