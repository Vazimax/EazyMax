from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,)

    def __str__(self):
        return self.name 

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

    def __str__(self):
        return self.title
