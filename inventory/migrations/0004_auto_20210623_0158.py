# Generated by Django 3.2.4 on 2021-06-22 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210623_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomingstock',
            old_name='number_qty',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='incomingstock',
            old_name='qty',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='number_qty',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='qty',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='in_stock',
            new_name='available',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='qty',
            new_name='quantity',
        ),
    ]