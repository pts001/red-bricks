from django.shortcuts import render, redirect
from .models import Restaurants, Reviews
from django.db.models import Avg
from .forms import ReviewPostForm
from django.views.generic import ListView, DetailView


class HomeView(ListView):

    model = Restaurants
    template_name = 'redbricks/home.html'
    context_object_name = 'restaurants'


class RestaurantsViews(DetailView):

    model = Restaurants
    context_object_name = 'restaurant'
    template_name = 'redbricks/view_restaurant.html'


def restaurents(request,id):
    restaurant = Restaurants.objects.get(pk=id)
    reviews = Reviews.objects.filter(restaurant=restaurant)
    avg_rating = reviews.aggregate(Avg('ratings'))
    # reviewer = reviews.reviewer
    context = {'restaurant':restaurant,
               'avg_ratings':avg_rating,
               'reviews':reviews}
    return render(request, 'redbricks/view_restaurant.html', context)


def post_review(request, id):
    restaurant = Restaurants.objects.get(pk=id)
    if request.method == 'POST':
        review = Reviews(ratings=request.POST['ratings'],comments=request.POST['review'],reviewer=request.user, restaurant=restaurant)
        review.save()
    return render(request,'redbricks/view_restaurant.html')
