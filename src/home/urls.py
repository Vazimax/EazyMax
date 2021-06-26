from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('plumber/',plumber,name="plumber"),
    path('electrician/',electrician,name="electrician"),
    path('childcare/',childcare,name="childcare"),
    path('porter/',porter,name="porter"),
    path('teaching/',teaching,name="teaching"),
]   