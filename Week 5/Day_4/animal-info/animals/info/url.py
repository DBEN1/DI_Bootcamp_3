from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.animals, name='animals'),
    path('families/', views.families, name='families'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('animal_in_family/<int:pk>/', views.animal_in_family, name='animal_in_family'),
]
