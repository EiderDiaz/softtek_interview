from django.http.response import HttpResponse
from django.shortcuts import render
from .models import detecting_change
from .forms import WeatherChangeForm
import pandas as pd

# Create your views here.

def weather(request):
    if request.method == "GET":
        #get wheather data from dataset 
        weather_data = detecting_change.objects.all()
        form = WeatherChangeForm()
        return render(request,'weather_change.html',{"weather_data":weather_data,"form":form })
    elif request.method == "POST":
        form = WeatherChangeForm(request.POST)
        #bleach is for cleaning the data in order counter measure for attacks
        weather_data = detecting_change.objects.all()
        if form.is_valid():
            is_good_to_bad = form.cleaned_data["is_good_to_bad"]
            #results =  pd.DataFrame(list(detecting_change.objects.all().values()))
            #response = HttpResponse(content_type='text/csv')
            #response['Content-Disposition'] = 'attachment; filename=filename.csv'
            #results.to_csv(path_or_buf=response,sep=',',index=False,decimal=",")
            #return response
            result = detect_weather_change(is_good_to_bad)
            print(result)

            return render(request,'weather_change.html', {"weather_data":weather_data,"success":True,
             "form":form,"result":result } )
    else:
        raise NotImplementedError
        render()
    return render(request, 'weather_change.html', {"form":form})

def detect_weather_change(is_good_to_bad):
    #get all the vañues of the weather table to dataframe
    df = pd.DataFrame(list(detecting_change.objects.all().values()))
    #get the ones who are not equal (ne) with respect of the previous one (shift)
    df["weather_change"] = df.was_rainy.ne(df.was_rainy.shift())
    #get the ones who change and were rainy
    if is_good_to_bad :
        result = df[ df["was_rainy"] & df["weather_change"]]
    else:
        result = df[-df["was_rainy"] & df["weather_change"]]

    return result
     







def customer(request):
    return render(request,'customer_order_status.html')

def seasons(request):
    return render(request,'seasons.html')