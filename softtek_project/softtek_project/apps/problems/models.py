from django.db import models

# Create your models here
class detecting_change(models.Model):
    date = models.DateField(blank=False,null=False)
    was_rainy = models.BooleanField(blank=False,null=False)
