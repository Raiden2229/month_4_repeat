from django.urls import path
from . import views

urlpatterns = [
    path('first_products/', views.first_products),
    path('second_products/', views.second_products),
    path('third_products/', views.third_products),
    path('current_time/', views.data_time),
]