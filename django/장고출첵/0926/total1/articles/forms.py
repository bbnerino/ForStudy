from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'