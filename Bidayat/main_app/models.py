from django.db import models
from django.contrib.auth.models import User

ROLE = (('C', 'Customer'), ('V', 'Vendor'))
SERVICE = (('1', 'BAKER'), ('2', 'PHOTOGRAPHER'))

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=ROLE, default=ROLE[0][0])
    image = models.ImageField(upload_to="main_app/static/uploads", default="")
    service = models.CharField(max_length=1, choices=SERVICE, default=SERVICE[0][0])
