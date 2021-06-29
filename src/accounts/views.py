from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login
from django.shortcuts import redirect, render 
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from jobs.models import Job
from .models import Profile
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request,'Your account has been CREATED :)')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(f'/accounts/profile/{user.id}')

    else :
        form = SignupForm()

    context = {
        'form' : form,
    }
    return render(request,'registration/signup.html',context)

@login_required
def profile(request,id):
    profile = Profile.objects.get(user=id)

    posts = Job.objects.filter(poster_id=id)
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'profile' : profile, 
        'posts' : page_obj,
    }
    return render(request,'profile/profile.html',context)


@login_required
def profile_edit(request,id):
    profile = Profile.objects.get(user=id)
    
    if request.method == 'POST':
        u_form = UserForm(request.POST,instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            my_profile = p_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(f'/accounts/profile/{profile.id}')


    else :
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request,'profile/profile_edit.html',context)
