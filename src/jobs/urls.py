from django.urls import path
from .views import *
from .api import *

app_name = 'jobs'

urlpatterns = [
    path('',job_list,name="job_list"),
    path('post_job/',post_job,name="post_job"),
    path('<str:slug>/',job_detail,name="job_detail"),
    path('<str:id>/add_comment/',add_comment,name="add_comment"),
    path('api/list/',job_list_api,name="job_list_api"),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('api/job/<int:id>/',job_detail_api,name="job_detail_api"),
    path('api/list/v2/',JobListApi.as_view(),name="job_list_api"),
    path('api/job/<int:id>/v2/',JobDetail.as_view(),name="job_detail_api"),

]   