from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BMI
from .forms import BMIForm
# Create your views here.
def bmi_add_view(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            user = request.user
            gender = form.cleaned_data['gender']
            height = form.cleaned_data['height']
            n_height = height/100
            weight = form.cleaned_data['weight']
            rate_of_activity = form.cleaned_data['rate_of_activity']
            bmi = weight/(n_height**2)
            BMI.objects.create(
                user=user,
                gender=gender,
                height=height,
                weight=weight,
                rate_of_activity=rate_of_activity,
                bmi=bmi
            )
            return redirect('get_bmi')
    else:
        form = BMIForm()
    return render(request, 'bmi/bmi_add.html', {'form': form})

def get_bmi(request):
    user = request.user
    try:
        bmi = BMI.objects.get(user=user)
        form = BMIForm(instance=user)
    except BMI.DoesNotExist:
        return redirect('add_bmi')
    return render(request, 'bmi/bmi_calculator.html', {'form': form,'bmi':bmi})

def bmi_update_view(request, pk):
    bmi = get_object_or_404(BMI, pk=pk)
    
    if request.method == 'POST':
        form = BMIForm(request.POST, instance=bmi)
        if form.is_valid():
            user = request.user
            gender = form.cleaned_data['gender']
            height = form.cleaned_data['height']
            n_height = height/100
            weight = form.cleaned_data['weight']
            rate_of_activity = form.cleaned_data['rate_of_activity']
            bmi = weight/(n_height**2)
            BMI.objects.update(
                user=user,
                gender=gender,
                height=height,
                weight=weight,
                rate_of_activity=rate_of_activity,
                bmi=bmi
            )
            return redirect('get_bmi')
    else:
        form = BMIForm(instance=bmi)
    
    return render(request, 'bmi/bmi_update.html', {'form': form})