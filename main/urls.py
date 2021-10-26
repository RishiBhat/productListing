from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('home/',views.home, name="home"),
    path('display/',views.display, name="display"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete, name="delete"),   
    
    
    path('input_form/',views.input_form, name="input_form"), 
    path('input_display/',views.input_display, name="input_display"),   
    path('input_updated/<int:id>',views.input_updated, name="input_updated"),   
    path('input_delete/<int:id>',views.input_delete, name="input_delete"),   
    
]
