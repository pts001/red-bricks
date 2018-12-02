from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Restaurants, Reviews
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView


# Function-based Home View for RedBricks App
def home(request):
    restaurants = Restaurants.objects.all()
    res_kol = Restaurants.objects.filter(city='Kolkata')
    res_blr = Restaurants.objects.filter(city='Bangalore')
    res_chn = Restaurants.objects.filter(city='Chennai')
    res_dlh = Restaurants.objects.filter(city='Delhi')
    veg = Restaurants.objects.filter(category='Veg Only')
    chinese = Restaurants.objects.filter(category='Chinese')
    south = Restaurants.objects.filter(category='South Indian')
    north = Restaurants.objects.filter(category='North Indian')
    context={'restaurants':restaurants,
             'res_kol':res_kol,
             'res_blr': res_blr,
             'res_chn': res_chn,
             'res_dlh': res_dlh,
             'veg':veg,
             'chinese':chinese,
             'south':south,
             'north':north}
    return render(request,'redbricks/home.html',context)


# View for each individual restaurant in database
def restaurents(request,id):
    restaurant = Restaurants.objects.get(pk=id)
    reviews = Reviews.objects.filter(restaurant=restaurant).order_by('-date_posted')
    avg_rating = reviews.aggregate(Avg('ratings'))
    # reviewer = reviews.reviewer
    context = {'restaurant':restaurant,
               'avg_ratings':avg_rating,
               'reviews':reviews}
    return render(request, 'redbricks/view_restaurant.html', context)


# restaurants by category
def restaurants_by_category(request, category):
    restaurants = Restaurants.objects.filter(category=category).all()
    context = {
                'restaurants':restaurants,
                'heading':'{} {}'.format(category, 'Restaurant')
                }
    return render(request, 'redbricks/restaurants_by_category.html',context)


# restaurants by city
def restaurants_by_city(request, city):
    restaurants = Restaurants.objects.filter(city=city).all()
    context = {
                'restaurants':restaurants,
                'heading':'{} {}'.format('Restaurants in',city)
                }
    return render(request, 'redbricks/restaurants_by_category.html',context)


class CreateRatingsView(LoginRequiredMixin, CreateView):
    model = Reviews
    fields = ['ratings','comments']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_reviews'] = Reviews.objects.filter(reviewer= self.request.user)
        return context

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.instance.restaurant = Restaurants.objects.get(pk=self.kwargs['id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('redbricks-restaurant',kwargs={'id':self.kwargs['id']})


class UpdateRatingsView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Reviews
    fields = ['ratings','comments']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_reviews'] = Reviews.objects.filter(reviewer= self.request.user)
        return context

    def test_func(self):
        review = self.get_object()
        if review.reviewer == self.request.user:
            return True
        return False

    def get_success_url(self):
        return reverse('redbricks-restaurant',kwargs={'id':self.get_object().restaurant.pk})


def delete_review(request, id):
    review = Reviews.objects.get(pk=id)
    if review.reviewer == request.user:
        review.delete()
        return redirect('redbricks-restaurant', id=review.restaurant.pk)
    else:
        return HttpResponseForbidden()