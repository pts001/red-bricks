# Generated by Django 2.1.2 on 2018-10-28 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owners_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('contact_no', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(choices=[('Kolkata', 'Kolkata'), ('Bangalore', 'Bangalore'), ('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Indore', 'Indore'), ('Gurgaon', 'Gurgaon'), ('Bhubneswar', 'Bhubneswar')], default='Bangalore', max_length=20)),
                ('res_name', models.CharField(max_length=40)),
                ('restaurant_pic', models.ImageField(default='default.jpg', upload_to='restaurant_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=10)),
                ('comments', models.TextField(blank=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='redbricks.Restaurants')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
