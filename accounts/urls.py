from django.urls import path
from .import views

#from django.http import HttpResponse

urlpatterns = [
    path('',views.home),
    path('products/', views.products),
    path('customer/', views.customer),]

