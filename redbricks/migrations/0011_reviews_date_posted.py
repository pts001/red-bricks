# Generated by Django 2.1.2 on 2018-11-01 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('redbricks', '0010_auto_20181028_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
