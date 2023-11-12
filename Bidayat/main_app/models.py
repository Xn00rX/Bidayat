from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Messages(models.Model):
  email=models.EmailField(max_length=50)
  phoneNumber=models.CharField(max_length=13)
  budget=models.CharField(max_length=50)
  guestCount=models.CharField(max_length=30)
  eventType=models.CharField(max_length=50)
  eventDate=models.DateField()
  description=models.CharField(max_length=600)
  sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
  receiver=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')

  def get_absolute_url(self):
    return reverse('message_index')
from django.contrib.auth.models import User

ROLE = (('C', 'Customer'), ('V', 'Vendor'))
SERVICE = (('1', 'BAKER'), ('2', 'PHOTOGRAPHER'))

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='Profile')
    type = models.CharField(max_length=1, choices=ROLE, default=ROLE[0][0])
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    service = models.CharField(max_length=1, choices=SERVICE, default=SERVICE[0][0])
