from django.db import models
from users.models import user
# Create your models here.
class BMI(models.Model):
    gender = (
        ('male','male'),
        ('female','female'),
    )
    activity = (
        ('Sedentary','sedentary'),
        ('Little/No exercise','Little/No exercise'),
        ('Low activity (exercise 1-3 times/week)','Low activity (exercise 1-3 times/week)'),
        ('Active (daily exercise or intense exercise 3-4 times/week)','Active (daily exercise or intense exercise 3-4 times/week)'),
        ('High activity (intense exercise 6-7 times/week)','High activity (intense exercise 6-7 times/week)'),
        ('Very high activity (very intense exercise daily, or physical job)','Very high activity (very intense exercise daily, or physical job)'),
    )
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100, choices=gender,null=True)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    rate_of_activity=models.CharField(max_length=100,choices=activity,null=True)
    bmi = models.DecimalField(decimal_places=3,max_digits=1000,blank=True)