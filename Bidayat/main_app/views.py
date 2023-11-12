from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Messages,User,Category, Work
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import CreateUserForm , ProfileSignUp,MessageForm
# Create your views here.

class WorkCreate(LoginRequiredMixin, CreateView):
  model = Work
  fields = ['title', 'description', 'worktype', 'category']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class WorkUpdate(LoginRequiredMixin, UpdateView):
  model = Work
  fields = ['title', 'description', 'worktype', 'category']

class WorkDelete(LoginRequiredMixin, DeleteView):
  model = Work
  success_url = '/works/'



  

class CategoryCreate(CreateView):
  model = Category
  fields = ['name', 'image']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)



class CategoryUpdate(UpdateView):
  model = Category
  fields = ['name', 'image']



class CategoryDelete(DeleteView):
  model = Category


def home(request):
  return render(request,'index.html')


def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
        return render(request, 'detail/user_detail.html', {'profile': profile})
    except User.DoesNotExist or Profile.DoesNotExist:
        return render(request, 'detail/user_not_found.html')



def about(request):
  return render(request, 'about.html')

class MessageList(ListView):
  model = Messages

class MessageCreate(CreateView):
  model = Messages
  fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']

  def form_valid(self,form):
    form.instance.sender = self.request.user
    return super().form_valid(form)


# def Message_Create(request,user_id):
#   form = MessageForm(request.POST)
#   if form.is_valid():
#     new_message = form.save(commit=False)
#     new_message.


class MessageUpdate(UpdateView):
  model = Messages
  fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']


def Message_detail(request,message_id):
  #SELECT * FROM 'main_app_cat' WHERE id = cat_id
  message = Messages.objects.get(id=message_id)
  return render(request, 'message/detail.html',{'message': message})

class MessageDelete(DeleteView):
  model = Messages
  success_url='/messages/'



# views.py
# views.py
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profileForm = ProfileSignUp(request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Signup'
            print(form.errors)  # Print form errors to console
            print(profileForm.errors)  # Print profileForm errors to console

    form = CreateUserForm()
    profileForm = ProfileSignUp()
    context = {'form': form, 'profileForm': profileForm, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
@login_required
def works_category(request, category_id):
  works = Work.objects.filter(category=category_id)
  categories = Category.objects.all()
  return render(request, 'works/categoryworks.html', {'works': works, 'categories': categories})


@login_required
def works_index(request):
  works = Work.objects.all()
  return render(request, 'works/index.html', {'works': works})


@login_required
def works_detail(request, work_id):
  work = Work.objects.get(id=work_id)
  return render(request, 'works/detail.html', {'work': work})



def categories_index(request):
  categories = Category.objects.all()
  return render(request, 'categories/index.html', {'categories': categories})

def categories_detail(request, category_id):
  categories = Category.objects.all()
  category = Category.objects.get(id=category_id)
  return render(request, 'categories/detail.html',{'category': category, 'categories': categories})

# def categories_base(request):
#   categories = Category.objects.all()
#   return render(request, 'base.html', {'categories': categories})




