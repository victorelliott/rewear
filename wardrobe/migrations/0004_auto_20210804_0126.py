# Generated by Django 3.2.5 on 2021-08-04 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0003_auto_20210804_0121'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DateWorn',
            new_name='WearDate',
        ),
        migrations.RenameField(
            model_name='weardate',
            old_name='date_worn',
            new_name='date',
        ),
    ]
