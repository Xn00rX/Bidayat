from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Work
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
  categories = Category.objects.all()
  return render(request,'index.html', {'categories': categories})

def about(request):
  categories = Category.objects.all()
  return render(request, 'about.html', {'categories': categories})

@login_required
def works_category(request):
  works = Work.objects.filter(category=request.category_id)
  categories = Category.objects.all()
  return render(request, 'works/categoryworks.html', {'works': works, 'categories': categories})


@login_required
def works_index(request):
  works = Work.objects.all()
  categories = Category.objects.all()
  return render(request, 'works/index.html', {'works': works, 'categories': categories})


@login_required
def works_detail(request, work_id):
  work = Work.objects.get(id=work_id)
  categories = Category.objects.all()
  return render(request, 'works/detail.html', {'work': work, 'categories': categories})



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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup Attempt', form.error_messages

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


