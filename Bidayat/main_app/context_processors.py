from django.http import HttpResponse
from .models import Category,Messages


def add_variable_to_context(request):
    categories = Category.objects.all()
    return {'categories': categories}


def messages_num(request):
    messages = Messages.objects.filter(receiver_id=request.user,reply=False).count()
