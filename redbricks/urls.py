from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('',HomeView.as_view(), name= 'redbricks-home'),
    path('restaurant/<int:id>',views.restaurents, name= 'redbricks-restaurant'),
    path('restaurant/<int:id>/post_review',views.post_review, name= 'redbricks-review'),
]