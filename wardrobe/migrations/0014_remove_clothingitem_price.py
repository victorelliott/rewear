# Generated by Django 3.2.5 on 2021-08-19 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0013_auto_20210819_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothingitem',
            name='price',
        ),
    ]
