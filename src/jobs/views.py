from django.core import paginator
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .forms  import JobForm,ApplyForm
from .models import *


def job_list(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
    }
    return render(request,'jobs/job_list.html',context)

def job_detail(request,slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST' :
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job
            my_form.save()
    else :
        form = ApplyForm

    context = {
        'job' : job,
        'form' : form
    }
    return render(request,'jobs/job_detail.html',context)


def post_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.poster = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else :
        form = JobForm()

    context = {
        'form' : JobForm()
    }
    return render(request,'jobs/post_job.html',context)