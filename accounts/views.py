from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(requset):
     return HttpResponse('home')

def products(requset):
    return HttpResponse('products')

def customer(requset):
     return HttpResponse('customer')