from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login
from django.shortcuts import redirect, render 
from django.urls import reverse
from .models import Profile
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')

    else :
        form = SignupForm()

    context = {
        'form' : form,
    }
    return render(request,'registration/signup.html',context)


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    context = {
        'profile' : profile,
    }
    return render(request,'profile/profile.html',context)


@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        u_form = UserForm(request.POST,instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            my_profile = p_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(reverse('accounts:profile'))

    else :
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request,'profile/profile_edit.html',context)
