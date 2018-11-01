from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    current_city = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(default='default_profile_pic.jpg',upload_to='user_profile_pic')

    def __str__(self):
       return '{} {} {}'.format(self.user.username, self.name, self.current_city)

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        output_size = (300,300)
        img.thumbnail(output_size)
        img.save(self.image.path)