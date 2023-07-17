from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bmi, name='get_bmi'),
    path('add_bmi/', views.bmi_add_view, name='add_bmi'),
    path('update_bmi/<int:pk>', views.bmi_update_view, name='update_bmi'),
]