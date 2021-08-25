from django.shortcuts import render
from .models import detecting_change
# Create your views here.

def weather(request):
    if request.method == "GET":
        #get wheather data from dataset 
        weather_data = detecting_change.objects.all()

        return render(request,'weather_change.html',{"weather_data":weather_data})
    elif request.method == "POST":

        #cambiar el contactform y crear uno para este
        #form = ContactForm(request.POST)
       #if form.is_valid():
       #    #bleach is for cleaning the data in order counter measure for attacks
       #    name = form.cleaned_data["name"]
       #    email = form.cleaned_data["email"]
       #    message = form.cleaned_data["message"]
        return render(request,'weather_change.html', {"success":True} )
    else:
        raise NotImplementedError
    return render(request, 'weather_change.html', {"form":form})





def customer(request):
    return render(request,'customer_order_status.html')

def seasons(request):
    return render(request,'seasons.html')