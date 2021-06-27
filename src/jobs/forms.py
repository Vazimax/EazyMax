from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from .models import Job ,Applying , Comment

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Applying
        fields = ['fullname','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['featured','slug','poster']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Write the name of the comment'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control','placeholder' : 'Write the details here'}),
        }