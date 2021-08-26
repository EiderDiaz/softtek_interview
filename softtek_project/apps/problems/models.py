from django.db import models

# Create your models here
class detecting_change(models.Model):
    date = models.DateField(blank=False,null=False)
    was_rainy = models.BooleanField(blank=False,null=False)


class CustomerOrderStatus(models.Model):

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
    status = models.CharField(blank=False,null=False,max_length=4, choices=ORDER_STATUS_CHOICES, default=PENDING)