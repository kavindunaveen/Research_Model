from django.urls import path
from . import views

urlpatterns = [
    path('', views.environmental_data_view, name='environmental_data'),
    path('temperature-chart/', views.temperature_chart, name='temperature_chart'),
    path('humidity-chart/', views.humidity, name='humidity'),
    path('luxlevel-chart/', views.luxlevel, name='luxlevel'),
    path('soil/', views.soil, name='soil'),
    path('co2/', views.co2, name='co2'),
    path('dataentry/', views.dataentry, name='dataentry'),
    

   
]
