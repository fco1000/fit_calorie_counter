from django.contrib import admin
from .models import (
    foodItem,
    userFoodItem,
    Category,
    Customer,
    calorie
)
# Register your models here.
class foodAdmin(admin.ModelAdmin):
    class Meta:
        model = foodItem
    list_display = ['name']
    list_filter = ['name']
    
admin.site.register(foodItem, foodAdmin)
admin.site.register(userFoodItem)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(calorie)
