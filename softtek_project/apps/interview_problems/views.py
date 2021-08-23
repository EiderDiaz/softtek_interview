from django.shortcuts import render

# Create your views here.

def weather(request):
    return render(request,'weather_change.html')

def customer(request):
    return render(request,'customer_order_status.html')

def seasons(request):
    return render(request,'seasons.html')