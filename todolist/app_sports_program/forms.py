from django import forms
from .models import Item, Program

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['owner']


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        exclude = ['type','user']