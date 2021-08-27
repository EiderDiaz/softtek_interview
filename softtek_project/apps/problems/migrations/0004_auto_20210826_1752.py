# Generated by Django 3.0.7 on 2021-08-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20210826_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('ord_id', models.CharField(max_length=42, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='customerorderstatus',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Shipped'), (3, 'Cancelled')], default=1),
        ),
    ]
