from django.http import HttpResponse
from .models import Category


def add_variable_to_context(request):
    categories = Category.objects.all()
    return {'categories': categories}