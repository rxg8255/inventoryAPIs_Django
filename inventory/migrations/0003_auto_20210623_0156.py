# Generated by Django 3.2.4 on 2021-06-22 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210623_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomingstock',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sale',
            name='number_qty',
            field=models.IntegerField(default=0),
        ),
    ]
