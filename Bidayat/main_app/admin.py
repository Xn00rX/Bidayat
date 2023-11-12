from django.contrib import admin
from .models import Messages,Profile,Work,Category
# Register your models here.
admin.site.register(Profile)

admin.site.register(Messages)
admin.site.register(Category)
admin.site.register(Work)
