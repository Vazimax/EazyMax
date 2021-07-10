from django.views.generic import DeleteView , UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django_filters import filters
from django.contrib import messages
from .forms  import JobForm,ApplyForm,CommentForm
from .filters import JobFilter
from .models import *
import random 


def job_list(request):
    jobs = Job.objects.all()

    filter = JobFilter(request.GET,queryset=jobs)
    jobs = filter.qs

    paginator = Paginator(jobs,9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs' : page_obj,
        'filter' : filter
    }
    return render(request,'jobs/job_list.html',context)

def job_detail(request,id):
    job = Job.objects.get(id=id)

    jobs = list(Job.objects.all())
    recent_jobs = random.sample(jobs,5)

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
        'form' : form,
        'jobs' : recent_jobs,
    }
    return render(request,'jobs/job_detail.html',context)

@login_required
def post_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.poster = request.user
            my_form.save()
            messages.success(request,'You created a post successefully')
            return redirect(reverse('jobs:job_list'))
    else :
        form = JobForm()

    context = {
        'form' : JobForm()
    }
    return render(request,'jobs/post_job.html',context)

# -----IMPORTANT------

@login_required
def add_comment(request,id):    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job_id = id
            my_form.save()
            messages.success(request,'You created a comment successefully')
            return redirect(f'/jobs/{id}/')


    else :
        form = CommentForm()

    context= {
        'form' : CommentForm()
    }
    return render(request,'jobs/add_comment.html',context)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Job
    fields = ['title','description','category','job_type']

    def form_valid(self,form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        else :
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Job
    #success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        else :
            return False