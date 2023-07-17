from django.urls import path
from django.views.generic import RedirectView
from .views import (
    userCreationView,
    userLoginView,
    userLogoutView,
    userChangeView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', RedirectView.as_view(url='register/', permanent=False)), 
    path('register/',userCreationView,name='register'),
    path('login/',userLoginView.as_view(),name='login'),
    path('logout/',userLogoutView.as_view(),name='logout'),
    path('update_user/',userChangeView.as_view(),name='user_update'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]