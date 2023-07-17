from django.shortcuts import render,redirect
from .models import (
    Category,
    Customer,
    foodItem,
    userFoodItem
)
from django.http import HttpResponse    
from users.models import user as user
from .forms import adduserFoodItemForm,FoodItemForm
from django.contrib.auth.decorators import login_required
from users.decorators.decorators import admin_only,allowed_users
from .filters import foodItemFilter
# Create your views here.

@login_required(login_url='login')
@admin_only
def homeView(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5] if Category.objects.filter(name='breakfast').exists() else []
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5] if Category.objects.filter(name='lunch').exists() else []
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5] if Category.objects.filter(name='dinner').exists() else []
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5] if Category.objects.filter(name='snacks').exists() else []
    customers = Customer.objects.all()
    context = {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snacks': snacks,
        'customers': customers,
    }
    return render(request, 'fit/main.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def foodItemView(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5] if Category.objects.filter(name='breakfast').exists() else []
    bcnt = len(breakfast)
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5] if Category.objects.filter(name='lunch').exists() else []
    lcnt = len(lunch)
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5] if Category.objects.filter(name='dinner').exists() else []
    dcnt = len(dinner)
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5] if Category.objects.filter(name='snacks').exists() else []
    scnt = len(snacks)

    context = {
        'breakfast':breakfast,
        'bcnt':bcnt,
        'lunch':lunch,
        'lcnt':lcnt,
        'dinner':dinner,
        'dcnt':dcnt,
        'snacks':snacks,
        'scnt':scnt,
    }
    
    return render(request, 'fit/food_item.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createFoodItemView(request):
    form = FoodItemForm()
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'fit/create_food_item.html', {'form':form})

@login_required(login_url='login')
def addFoodItemView(request):
    if request.user.is_authenticated:
        user = request.user
        cust = user.customer   
        form = adduserFoodItemForm()
        if request.method == 'POST':
            form = adduserFoodItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'fit/add_food_item.html', {'form':form})
    else:
        return redirect('login')

def userPageView(request):
    if request.user.is_authenticated:
        user = request.user
        if hasattr(user, 'customer'):
            cust = user.customer 
            foodItems = foodItem.objects.filter()
            myFilter = foodItemFilter(request.GET,queryset=foodItems)
            foodItems = myFilter.qs
            total = userFoodItem.objects.all()
            myFoodItems = total.filter(customer = cust)
            Count = myFoodItems.count()
            querysetFood = []
            for food in myFoodItems:
                querysetFood.append(food.fooditem.all())
            finalFoodItems = []
            for items in querysetFood:
                for food_items in items:
                    finalFoodItems.append(food_items)
            totalCalories = 0
            for foods in finalFoodItems:
                totalCalories += foods.calorie
            caloriesLeft = 2000 - totalCalories
        else:
            cust = None
            foodItems = []
            myFilter = None
            Count = 0
            finalFoodItems = []
            totalCalories = 0
            caloriesLeft = 2000
    else:
            cust = None
            foodItems = []
            myFilter = None
            Count = 0
            finalFoodItems = []
            totalCalories = 0
            caloriesLeft = 2000
    context = {
        'CalorieLeft':caloriesLeft,
        'totalCalories':totalCalories,
        'cnt':Count,
        'foodlist':finalFoodItems,
        'fooditem':foodItems,
        'myfilter':myFilter
    }
    return render(request, 'fit/user_page.html', context)
            