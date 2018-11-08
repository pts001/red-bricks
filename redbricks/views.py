from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Restaurants, Reviews
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView


def home(request):
    restaurants = Restaurants.objects.all()
    res_kol = Restaurants.objects.filter(city='Kolkata')
    res_blr = Restaurants.objects.filter(city='Bangalore')
    context={'restaurants':restaurants,
             'res_kol':res_kol,
             'res_blr': res_blr}
    return render(request,'redbricks/home.html',context)


def res_kolkata(request):
    restaurants = Restaurants.objects.filter(city='Kolkata')
    context={'restaurants':restaurants}
    return render(request,'redbricks/home.html',context)


def restaurents(request,id):
    restaurant = Restaurants.objects.get(pk=id)
    reviews = Reviews.objects.filter(restaurant=restaurant).order_by('-date_posted')
    avg_rating = reviews.aggregate(Avg('ratings'))
    # reviewer = reviews.reviewer
    context = {'restaurant':restaurant,
               'avg_ratings':avg_rating,
               'reviews':reviews}
    return render(request, 'redbricks/view_restaurant.html', context)


class CreateRatingsView(LoginRequiredMixin, CreateView):
    model = Reviews
    fields = ['ratings','comments']

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.instance.restaurant = Restaurants.objects.get(pk=self.kwargs['id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('redbricks-restaurant',kwargs={'id':self.kwargs['id']})


class UpdateRatingsView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Reviews
    fields = ['ratings','comments']

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