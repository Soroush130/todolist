from django import forms
from .models import Tag, TypeWork, Work


class NewWork(forms.ModelForm):
    class Meta:
        model = Work
        exclude = ['user', 'is_finished']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ['user']

