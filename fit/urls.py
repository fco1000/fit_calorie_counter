from django.urls import path
from .views import (
    homeView,
    userPageView,
    createFoodItemView,
    foodItemView,
    addFoodItemView,
)

urlpatterns = [
    path('',userPageView,name='user_page'),
    path('fit/admin/',homeView,name='home'),
    path('create_food_item/',createFoodItemView,name='createFoodItem'),
    path('product/',foodItemView,name='foodItem'),
    path('add_food_item/',addFoodItemView,name='addFoodItem'),
]