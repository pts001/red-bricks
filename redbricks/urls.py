from django.urls import path
from . import views
from .views import CreateRatingsView, UpdateRatingsView

urlpatterns = [
    path('',views.home, name= 'redbricks-home'),
    path('kolkata/',views.res_kolkata, name= 'redbricks-kol'),
    path('restaurant/<int:id>',views.restaurents, name= 'redbricks-restaurant'),
    path('restaurant/<int:id>/post_review',CreateRatingsView.as_view(), name= 'redbricks-review'),
    path('reviews/<int:pk>/update',UpdateRatingsView.as_view(), name= 'redbricks-review-update'),
    path('reviews/<int:id>/delete',views.delete_review, name= 'redbricks-review-delete'),
]