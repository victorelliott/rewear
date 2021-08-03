# Generated by Django 3.2.5 on 2021-08-03 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_worn', models.DateField()),
                ('garments', models.ManyToManyField(to='wardrobe.Garment')),
            ],
        ),
    ]
