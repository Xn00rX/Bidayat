from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile,Messages

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class ProfileSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','type','service']
        
  

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  

class CustomerSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
        
class VendorSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','service']

       
class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']