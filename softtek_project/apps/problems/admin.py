from django.contrib import admin

# Register your models here.
from .models import detecting_change,CustomerOrderStatus,Season

admin.site.register(detecting_change)
admin.site.register(CustomerOrderStatus)
admin.site.register(Season)

