# Generated by Django 2.2.5 on 2020-01-15 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0002_auto_20200115_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='superhost',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]