# Generated by Django 2.2.5 on 2020-01-15 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_room_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='room',
            name='instant_book',
            field=models.BooleanField(default=False),
        ),
    ]