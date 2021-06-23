from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [
    path('',job_list,name="job_list"),
    path('post_job/',post_job,name="post_job"),
    path('<str:slug>/',job_detail,name="job_detail"),
]