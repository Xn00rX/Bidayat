from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)


  def get_absolute_url(self):
    return reverse('workdetail', kwargs={'work_id' : self.id})
    
  def __str__(self):
    return f"{self.title}"
