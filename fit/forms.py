from .models import foodItem,userFoodItem
from django import forms

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = foodItem
        fields = '__all__'
        
class adduserFoodItemForm(forms.ModelForm):
    class Meta:
        model = userFoodItem
        fields = ['fooditem' ] 
        labels = ['Food item' ]     
        widgets = {
            'fooditem': forms.SelectMultiple(attrs={'class':'form-control'}),
        }  
