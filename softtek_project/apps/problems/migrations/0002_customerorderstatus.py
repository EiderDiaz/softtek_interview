# Generated by Django 3.0.7 on 2021-08-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=16)),
                ('item_name', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('PEND', 'Pending'), ('SHIP', 'Shipped'), ('CANC', 'Cancelled')], default='PEND', max_length=4)),
            ],
        ),
    ]
