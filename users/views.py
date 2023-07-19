from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login
from .models import user
from .forms import UserSignUpForm,UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import Group
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from fit.models import Customer
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def userCreationView(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        group = Group.objects.get(name='user')
        User = user.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        User.groups.add(group)
        login(request,User)
        Customer.objects.create(
            user=User, 
            name=username,
            email=email
        )
        message = 'Welcome to Fit Calorie Calculator \n Thank you for choosing us to help you in your journey of getting/keeping fit(We don\'t judge) \n We hope you have a good time and thanks for being a tester. \n Your feedback wil be highly valued'
        send_mail(  subject = 'Welcome to Fit',
                    message = message,
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [User.email, ],
                    fail_silently=False)
         
        messages.success(request, f'{User.username}\'s account creation successful.Please verify your email')
        return redirect('user_page')        
    else:
        return render(request, 'users/register_user.html', {'form': form})

class userChangeView(View):
    def get(self,request):
        form= UserChangeForm()
        return render(request, 'users/register_user.html', {'form': form})
        
    def post(self,request):
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/update_user.html', {'form': form}) 
    
class userLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'users/logout_user.html'
    
    def get_success_url(self):
        return reverse('login') 

class userLoginView(LoginView):
    template_name = 'users/login_user.html'
    
    def get_success_url(self):
        return reverse('user_page') 
