from django.db import models
from users.models import user
# Create your models here.
class calorie(models.Model):
    users = models.OneToOneField(user,null=True,on_delete=models.CASCADE)
    calories = models.IntegerField()
    
    def __str__(self):
        return f'{self.user} - {self.calories}'
    
class Customer(models.Model):
    user = models.OneToOneField(user,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    options = (
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks')
    )
    name = models.CharField(max_length=50,choices=options)
    
    def __str__(self):
        return str(self.name)
    
class foodItem(models.Model):
    name = models.CharField(max_length=200)
    carbohydrate = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fats = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    protein = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return str(self.name)
    
#for user page-------------------------------------------------------------
class userFoodItem(models.Model):
    customer = models.ManyToManyField(Customer ,blank=True)
    fooditem=models.ManyToManyField(foodItem)
    created_at=models.DateTimeField(blank=True,auto_now_add=True,null=True)