from django.contrib import admin
from django.urls import path
from . import views

app_name = 'trucks' 
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.truck_list, name="truck_list"),
    path('reset/', views.reset_data, name='reset_data'),
]