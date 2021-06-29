from django import forms
from .models import Job
import django_filters

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control text-white text-center'}))

    class Meta:
        model = Job
        fields = ['title','job_type','category']

class JobFilter2(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title','job_type']
