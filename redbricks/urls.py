from django.urls import path
from . import views
from .views import CreateRatingsView, UpdateRatingsView

urlpatterns = [
    path('',views.home, name= 'redbricks-home'),
    path('/about', views.about, name='redbricks-about'),
    path('by_category/<str:category>',views.restaurants_by_category, name= 'redbricks-by_category'),
    path('by_city/<str:city>',views.restaurants_by_city, name= 'redbricks-by_city'),
    path('restaurant/<int:id>',views.restaurents, name= 'redbricks-restaurant'),
    path('restaurant/<int:id>/post_review',CreateRatingsView.as_view(), name= 'redbricks-review'),
    path('reviews/<int:pk>/update',UpdateRatingsView.as_view(), name= 'redbricks-review-update'),
    path('reviews/<int:id>/delete',views.delete_review, name= 'redbricks-review-delete'),
]