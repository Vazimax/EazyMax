from django.urls import path
from .views import signup , profile , profile_edit

app_name="accounts"

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('profile/<int:id>/',profile,name="profile"),
    path('profile/<int:id>/edit/',profile_edit,name="profile_edit"),

]