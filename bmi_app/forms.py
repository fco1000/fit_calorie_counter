from django import forms
from .models import BMI

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ['gender','height','weight','rate_of_activity']
        labels = ['Gender','Height','Weight','Rate of activity']
        widgets = {
            'gender': forms.RadioSelect,
            'height': forms.NumberInput(attrs={'placeholder':'cm'}),
            'weight': forms.NumberInput(attrs={'placeholder':'kg'}),
            'rate_of_activity': forms.RadioSelect,
        }