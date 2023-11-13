from django.http import HttpResponse
from .models import Category
from .models import Profile



def add_variable_to_context(request):
    categories = Category.objects.all()
    return {'categories': categories}



from .models import Profile  


def navigation_links(request):
    user_authenticated = request.user.is_authenticated
    user_type = None
    if user_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            user_type = user_profile.type
        except Profile.DoesNotExist:
            user_type = None

    context = {
        'user_authenticated': user_authenticated,
        'user_type': user_type,
    }
    return context
    
