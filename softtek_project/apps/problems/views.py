from django.http.response import HttpResponse
from django.shortcuts import render
from .models import detecting_change,CustomerOrderStatus,Season
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
            weather_changed_df = detect_weather_change(is_good_to_bad)

            return render(request,'weather_change.html', {"weather_data":weather_data,"success":True,
             "form":form,"weather_changed_df":weather_changed_df } )
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
    #get order data from dataset 
    customer_order_status = CustomerOrderStatus.objects.all()
    
    if request.method == "GET":
        #render the page and pass the form and the data
        return render(request,'customer_order_status.html',{"customer_order_status":customer_order_status })
    elif request.method == "POST":
        #get wheather data from dataset 
        if 'btnform1' in request.POST:
            df = pd.DataFrame(list(customer_order_status.values()))
            #group the dataframe by ordername and get only the status column
            grouped_df = df.groupby(['order_number'])["status"]
            #since the hierarchy of the categorical ordinal values allows it just get the min od the grouped order
            overall_order_status_df = grouped_df.apply(lambda x: min(x)).to_frame()
            #rename the column to overall_status instead just 0
            overall_order_status_df= overall_order_status_df.set_axis(['overall_status'], axis='columns')
            #print(overall_order_status_df)
        return render(request,'customer_order_status.html', 
        {"customer_order_status":customer_order_status,"success":True, "overall_order_status_df":overall_order_status_df } )
    else:
        raise NotImplementedError
    return render(request, 'customer_order_status.html', {"form":form})

def seasons(request):
     #get order data from dataset 
    Season_qs = Season.objects.all()
    
    if request.method == "GET":
        #render the page and pass the form and the data
        return render(request,'seasons.html',{"Season_qs":Season_qs })
    elif request.method == "POST":
        #get wheather data from dataset 
        if 'btnform1' in request.POST:
            dates_df = pd.DataFrame(list(Season_qs.values()))
            doy = pd.to_datetime(dates_df['date']).dt.dayofyear
            season_df = pd.DataFrame(doy.apply(get_season_from_day))
            season_df["ord_id"] = dates_df["ord_id"]
            print(season_df)
            print(type(season_df))

        return render(request,'seasons.html', 
        {"Season_qs":Season_qs,"success":True,"season_df":season_df} )
    else:
        raise NotImplementedError
    return render(request, 'seasons.html', {"form":form})

# function that takes a given day of the given year and returns the season in which it belongs
def get_season_from_day(day_of_year):
    
  #lower bound for spring, parse the given bound to the given day of the year
  spring_low = pd.to_datetime("2021-march-19",format="%Y-%B-%d").dayofyear
  #upper bound for spring, parse the given bound to the given day of the year
  spring_up = pd.to_datetime("2021-june-19",format="%Y-%B-%d").dayofyear
  
  summer_low = pd.to_datetime("2021-june-20",format="%Y-%B-%d").dayofyear
  summer_up = pd.to_datetime("2021-september-21",format="%Y-%B-%d").dayofyear

  fall_low = pd.to_datetime("2021-september-22",format="%Y-%B-%d").dayofyear
  fall_up = pd.to_datetime("2021-december-20",format="%Y-%B-%d").dayofyear

  #print(spring_low,"-",spring_up)
  #print(summer_low,"-",summer_up)
  #print(fall_low,"-",fall_up)

  # create the range of values of a given season
  spring = range(spring_low, spring_up)
  summer = range(summer_low, summer_up)
  fall = range(fall_low, fall_up)
  # winter = everything else

  # and then check the given day of the year belongs to a given season 
  if day_of_year in spring:
    season = "Spring"
  elif day_of_year in summer:
    season = "Summer"
  elif day_of_year in fall:
    season = "Fall"
  else:
    season = "Winter"
  return season