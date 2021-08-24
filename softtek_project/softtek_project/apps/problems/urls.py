from django.urls import path
from . import views

app_name = "problems"
urlpatterns = [
    path("weather",views.weather,name="weather_change"),
    path("customer",views.customer,name="customer_order_status"),
    path("seasons",views.seasons,name="seasons"),


]