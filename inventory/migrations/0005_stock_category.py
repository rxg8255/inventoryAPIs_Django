# Generated by Django 3.2.4 on 2021-06-22 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210623_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
