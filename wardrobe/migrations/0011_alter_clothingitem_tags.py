# Generated by Django 3.2.5 on 2021-08-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0010_alter_clothingtag_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='wardrobe.ClothingTag'),
        ),
    ]