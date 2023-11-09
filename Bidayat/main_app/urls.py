from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns=[
  path('',views.home, name='home'),
  
  path('about/',views.about,name='about'),
  
  

  path('accounts/signup/',views.signup,name='signup'),
  
  path('change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]