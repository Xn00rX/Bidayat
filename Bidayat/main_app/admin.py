from django.contrib import admin
from .models import Category, Work
from .models import Messages,Profile


# Register your models here.
admin.site.register(Category)
admin.site.register(Work)
admin.site.register(Profile)
admin.site.register(Messages)
