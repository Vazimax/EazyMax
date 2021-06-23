from django import forms
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Job ,Applying

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Applying
        fields = ['fullname','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['featured','slug','poster']