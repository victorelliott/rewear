# Generated by Django 3.2.5 on 2021-08-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0009_auto_20210807_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingtag',
            name='category',
            field=models.CharField(choices=[('TY', 'Type'), ('BR', 'Brand'), ('CO', 'Color'), ('OT', 'Other')], max_length=200),
        ),
    ]
