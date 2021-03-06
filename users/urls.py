from django.urls import path
from . import views

urlpatterns = [
    path('profile/update/username',views.update_username, name= 'profile-update-username'),
    path('profile/update/email',views.update_email, name= 'profile-update-email'),
    path('profile/update/full_name',views.update_full_name, name= 'profile-update-name'),
    path('profile/update/city',views.update_city, name= 'profile-update-city'),
    ]