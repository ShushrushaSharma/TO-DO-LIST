from django import forms
from django.forms import ModelForm
from .models import *

class TodoForm(forms.ModelForm):
    # meta class provides additional information to the form
    class Meta:
        model=Todo
        fields='__all__'

