from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.db.models.fields import related
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100,)

    def __str__(self):
        return self.name 

def image_upload(instance , filename):
    imagename , extension = filename.split('.')

    return f"jobs/{instance.id}.{extension}"

class Job(models.Model):

    JOB_TYPE = (
        ('Full Time','Full Time'),
        ('Part Time','Part Time')
    )

    title = models.CharField(max_length=250)
    poster = models.ForeignKey(User,related_name='job_poster',on_delete=models.CASCADE)
    description = models.TextField(max_length=2000,blank=True,null=True)
    job_type = models.CharField(max_length=100,choices=JOB_TYPE,null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to=image_upload,default="jobs/default.jpg")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_posted',)


    def get_absolute_url(self):
        return reverse('jobs:job_detail',kwargs={'id':self.id})

    # def save(self):
    #     self.save()

    #     img = Image.open(self.image.path)

    #     if img.height > 500 or img.width > 500:
    #         output_size = (500,500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


class Comment(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name="comments",null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.job.title} / {self.name}")



class Applying(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply')
    cover_letter = models.TextField(max_length=1000) 
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname