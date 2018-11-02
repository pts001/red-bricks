from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from redbricks.models import Restaurants, Reviews
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'{} {}'.format('Account Created For',username))
            return redirect('redbricks-home')
    else:
        form = RegisterForm()
    return render(request,'users/register.html', {'form':form})


@login_required
def profile(request):
    my_reviews = Reviews.objects.filter(reviewer=request.user)
    context = {'my_reviews':my_reviews}
    return render(request, 'users/profile.html', context)


def update_email(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print(request.POST['email'])
    return render(request,'users/update_email.html')


def update_full_name(request):
    if request.method == 'POST':
        print(request.POST['full_name'])
    return render(request,'users/update_name.html')


def update_city(request):
    if request.method == 'POST':
        print(request.POST['city'])
    return render(request,'users/update_city.html')