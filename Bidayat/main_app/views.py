from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Messages
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.


def home(request):
  return render(request,'index.html')

def about(request):
  return render(request, 'about.html')

class MessageList(ListView):
  model = Messages

class MessageCreate(CreateView):
  model = Messages
  fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']

  def form_valid(self,form):
    form.instance.sender = self.request.user
    return super().form_valid(form)
  

class MessageUpdate(UpdateView):
  model = Messages
  fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']


def Message_detail(request,message_id):
  #SELECT * FROM 'main_app_cat' WHERE id = cat_id
  message = Messages.objects.get(id=message_id)
  return render(request, 'message/detail.html',{'message': message})

class MessageDelete(DeleteView):
  model = Messages
  success_url='/messages/'