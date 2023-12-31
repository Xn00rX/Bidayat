from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review

from .models import Profile,Messages

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class ProfileSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['type', 'service']


class CustomerSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
        
class VendorSignUp(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','service','view']

class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']