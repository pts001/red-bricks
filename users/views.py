from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfilePicForm
from redbricks.models import Reviews
from .models import UserProfile, User


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
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form=ProfilePicForm()
    context = {'form':form}
    return render(request, 'users/profile.html', context)


def update_username(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST['username']).first()
        if user:
            return HttpResponse(status=422)
        else:
            profile.user.username = request.POST['username']
            profile.user.save()
    return render(request,'users/update_username.html',{'profile':profile})


def update_email(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email']).first()
        if user:
            return HttpResponse(status=422)
        else:
            profile.user.email = request.POST['email']
            profile.user.save()
    return render(request,'users/update_email.html',{'profile':profile})


def update_full_name(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        profile.name = request.POST['full_name']
        profile.save()
    return render(request,'users/update_name.html')


def update_city(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        profile.current_city = request.POST['city']
        profile.save()
    return render(request,'users/update_city.html')