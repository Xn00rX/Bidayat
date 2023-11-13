from django.http import HttpResponse
from .models import Category,Messages,Profile



def add_variable_to_context(request):
    categories = Category.objects.all()
    return {'categories': categories}


def messages_num(request):
    messages = Messages.objects.filter(receiver_id=request.user,reply=False).count()
    return {'messages': messages}

from .models import Profile  


def navigation_links(request):
    user_authenticated = request.user.is_authenticated
    user_type = None
    if user_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            user_type = user_profile.type
            # messages = Messages.objects.filter(receiver_id=request.user,reply=False).count()
        except Profile.DoesNotExist:
            user_type = None
            
    context = {
        'user_authenticated': user_authenticated,
        'user_type': user_type,
        # 'messages':messages
    }
    

    return context
