from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Messages(models.Model):
  email=models.EmailField(max_length=50)
  phoneNumber=models.CharField(max_length=13)
  budget=models.CharField(max_length=50)
  guestCount=models.CharField(max_length=30)
  eventType=models.CharField(max_length=50)
  eventDate=models.DateField()
  description=models.CharField(max_length=600)
  sender=models.ForeignKey(User, on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse('message_index')
