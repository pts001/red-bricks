from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

# Choice Fields for cities
city_names = (('Kolkata','Kolkata'),
              ('Bangalore','Bangalore'),
              ('Delhi','Delhi'),
              ('Chennai','Chennai'))
categories = (('Chinese','Chinese'),
              ('South Indian','South Indian'),
              ('North Indian', 'North Indian'),
              ('Veg Only','Veg Only'))
ratings_choice = ((1,'1 star'),(2,'2 star'),(3,'3 star'),(4,'4 star'),(5,'5 star'))


# Model for restaurants
class Restaurants(models.Model):
    category = models.CharField(max_length=20, choices=categories, default='Veg Only')
    contact_no = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20,choices=city_names, default='Bangalore')
    res_name = models.CharField(max_length=40)
    restaurant_pic = models.ImageField(upload_to='restaurant_pic', default='default.jpg')

    def __str__(self):
        return '{} {}'.format(self.res_name, self.city)

    # resizing the uploaded image of restaurant
    def save(self):
        super().save()

        img = Image.open(self.restaurant_pic.path)
        output_size = (250,250)
        img.thumbnail(output_size)
        img.save(self.restaurant_pic.path)


# Review model for restaurant
# It has many-to-one ralationship with restaurants
class Reviews(models.Model):
    ratings = models.IntegerField(choices=ratings_choice)
    comments = models.TextField(null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} {} {}'.format(self.restaurant.res_name, self.ratings, self.comments)

