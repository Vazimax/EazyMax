from django.urls import path
from .views import *

urlpatterns = [
    path('job_list/',job_list,name="job_list"),
    path('<int:id>',job_list,name="job_list"),
    
]