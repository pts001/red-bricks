# Generated by Django 2.1.2 on 2018-10-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redbricks', '0006_auto_20181028_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_photos', models.ImageField(default='default.jpg', upload_to='restaurant_photos')),
                ('res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redbricks.Restaurants')),
            ],
        ),
    ]
