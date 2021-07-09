from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from jobs.models import Category

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to="profile/",default="profile/default.jpg")

    def __str__(self):
        return str(self.user)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
