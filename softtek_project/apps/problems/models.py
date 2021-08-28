from django.db import models

# Create your models here
class detecting_change(models.Model): #not pep-8 class definition, sorry i was on medication when i wrote that one :c
    date = models.DateField(blank=False,null=False)
    was_rainy = models.BooleanField(blank=False,null=False)


class CustomerOrderStatus(models.Model):
    #if the following hierarchy is established , where 1 is the most important and 3 the last,
    #if we wanna know the overall status we just get the min of the grouped order
    PENDING = 1
    SHIPPED  = 2
    CANCELLED  = 3
    
    ORDER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (CANCELLED, 'Cancelled'),
    ]
    order_number = models.CharField(blank=False,null=False,max_length=16)
    item_name = models.CharField(blank=False,null=False,max_length=120)
    status = models.IntegerField(blank=False,null=False, choices=ORDER_STATUS_CHOICES, default=PENDING)

class Season(models.Model):
    ord_id =  models.CharField(blank=False,null=False,max_length=42, primary_key=True)
    date = models.DateField(blank=False,null=False)

