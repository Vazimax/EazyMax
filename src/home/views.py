from django.shortcuts import render
from jobs.models import Category, Job 
from accounts.models import Profile
from jobs.filters import JobFilter ,JobFilter2
from django.core.paginator import Paginator
import random 

def home(request):
    jobs = list(Job.objects.all())
    recent_jobs = random.sample(jobs,5)

    jobs = Job.objects.all()
    filter = JobFilter(request.GET,queryset=jobs)
    jobs = filter.qs

    profiles = Profile.objects.all()

    context = {
        'recent_jobs' : recent_jobs,
        'filter' : filter,
        'profiles' : profiles,
    }
    return render(request,'home.html',context)

def about(request):

    return render(request,'about.html')

def plumber(request):
    jobs = Job.objects.filter(category=1)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/plumber.html',context)

def electrician(request):
    jobs = Job.objects.filter(category=2)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/plumber.html',context)

def childcare(request):
    jobs = Job.objects.filter(category=3)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/childcare.html',context)

def porter(request):
    jobs = Job.objects.filter(category=4)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter
    }
    return render(request,'categories/porter.html',context)

def teaching(request):
    jobs = Job.objects.filter(category=5)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/teaching.html',context)

def carpenter(request):
    jobs = Job.objects.filter(category=6)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/carpenter.html',context)

def painter(request):
    jobs = Job.objects.filter(category=7)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/painter.html',context)


def builder(request):
    jobs = Job.objects.filter(category=8)

    filter = JobFilter2(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter,
    }
    return render(request,'categories/builder.html',context)