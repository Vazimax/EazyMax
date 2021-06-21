from django.db import models
from PIL import Image

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
    description = models.TextField(default="What ill do : \nExperience : \nPrice : ",max_length=2000,blank=True,null=True)
    job_type = models.CharField(max_length=100,choices=JOB_TYPE,null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload,default="jobs/default.jpg")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

