from django import forms
from .models import WaterDaily

class WaterDailyForm(forms.ModelForm):
    class Meta:
        model = WaterDaily
        fields = ['count', 'date']