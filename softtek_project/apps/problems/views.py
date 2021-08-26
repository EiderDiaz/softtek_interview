from django.http.response import HttpResponse
from django.shortcuts import render
from .models import detecting_change,CustomerOrderStatus
from .forms import WeatherChangeForm
import pandas as pd

# Create your views here.

def weather(request):
    if request.method == "GET":
        #get wheather data from dataset 
        weather_data = detecting_change.objects.all()
        #instanciate the form
        form = WeatherChangeForm()
        #render the page and pass the form and the data
        return render(request,'weather_change.html',{"weather_data":weather_data,"form":form })
    elif request.method == "POST":
        #instanciate the form with the post request
        form = WeatherChangeForm(request.POST)
        #get wheather data from dataset 
        weather_data = detecting_change.objects.all()
        #if the form is valid, we get the flag to determine the dates in which the weather became bad or good
        # pass it to the func detect_weather_change
        if form.is_valid():
            is_good_to_bad = form.cleaned_data["is_good_to_bad"]
            result = detect_weather_change(is_good_to_bad)
            print(result)

            return render(request,'weather_change.html', {"weather_data":weather_data,"success":True,
             "form":form,"result":result } )
    else:
        raise NotImplementedError
    return render(request, 'weather_change.html', {"form":form})

def detect_weather_change(is_good_to_bad):
    #get all the values of the weather table to dataframe
    df = pd.DataFrame(list(detecting_change.objects.all().values()))
    #get the ones who are not equal (ne) with respect of the previous one (shift)
    df["weather_change"] = df.was_rainy.ne(df.was_rainy.shift())
    #determine the dates in which the weather became bad (the given day was rainy and changed with respect of the previous)
    if is_good_to_bad :
        result = df[ df["was_rainy"] & df["weather_change"]]
    #determine the dates in which the weather became good 
    else:
        result = df[-df["was_rainy"] & df["weather_change"]]
    return result
     



def customer(request):

    if request.method == "GET":
        #get order data from dataset 
        customer_order_status = CustomerOrderStatus.objects.all()
        #render the page and pass the form and the data
        return render(request,'customer_order_status.html',{"customer_order_status":customer_order_status })
    elif request.method == "POST":
        #get wheather data from dataset 
        customer_order_status = CustomerOrderStatus.objects.all()
        return render(request,'customer_order_status.html', {"customer_order_status":customer_order_status,"success":True } )
    else:
        raise NotImplementedError
    return render(request, 'customer_order_status.html', {"form":form})

def seasons(request):
    return render(request,'seasons.html')