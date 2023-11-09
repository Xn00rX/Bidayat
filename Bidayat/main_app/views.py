from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView,DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import CreateUserForm , ProfileSignUp

# Create your views here.


def home(request):
  return render(request,'index.html')

def about(request):
  return render(request, 'about.html')




# views.py
# views.py
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profileForm = ProfileSignUp(request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Signup'
            print(form.errors)  # Print form errors to console
            print(profileForm.errors)  # Print profileForm errors to console

    form = CreateUserForm()
    profileForm = ProfileSignUp()
    context = {'form': form, 'profileForm': profileForm, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

