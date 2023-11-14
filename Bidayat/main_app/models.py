from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Messages(models.Model):
  email= models.EmailField(max_length=50)
  phoneNumber= models.CharField(max_length=13)
  budget = models.CharField(max_length=50,default='-')
  guestCount = models.CharField(max_length=30,default='-')
  eventType = models.CharField(max_length=50,default='-')
  eventDate = models.DateField(default=date.today)
  description = models.CharField(max_length=600)
  sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
  reply = models.BooleanField(default=False)

  def get_absolute_url(self):
    return reverse('message_index')

ROLE = (('C', 'Customer'), ('V', 'Vendor'))
SERVICE = (('1', 'Baker'), ('2', 'Photographer'),
            ('3','Event Planner'),('4','Florist'),
            ('5','Invitations and Prints Company'),
            ('6','Caterer'),('7','Decor Company'),
            ('8','Stylist'),('9','Staffing Company'),
            ('10','Venues'),('11','Parking and Transportation Company'))

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='Profile')
    type = models.CharField(max_length=1, choices=ROLE, default=ROLE[0][0])
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    service = models.CharField(max_length=2, choices=SERVICE, default=SERVICE[0][0])
    view= models.CharField(max_length=500 , default="none")

    def __str__(self):
      return f"{self.user_id} {self.get_service_display()} {self.image}"



# Create your models here.


class Category(models.Model):
  name = models.CharField(max_length=50)  
  image = models.ImageField(upload_to = "main_app/static/uploads", default="")


  def __str__(self):
    return f"{self.name}"


class Work(models.Model):
  title = models.CharField(max_length=100) 
  description = models.TextField(max_length=250)
  worktype = models.CharField(max_length=80) 
  users = models.ManyToManyField(User)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="main_app/static/uploads", default="none.jpg",null=True, blank=True) 


  def get_absolute_url(self):
    return reverse('workdetail', kwargs={'work_id' : self.id})
    
  def __str__(self):
    return f"{self.users}{self.title}"


class WorkImage(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='main_app/static/uploads') 