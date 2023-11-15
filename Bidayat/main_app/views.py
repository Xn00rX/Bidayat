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

# * means to import everything from the following module

from .models import *      



from .forms import *
# Create your views here.

class WorkCreate(LoginRequiredMixin, CreateView):
    model = Work
    fields = ['title', 'description', 'worktype', 'category','users', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        

        if 'images' in self.request.FILES:
            for image in self.request.FILES.getlist('images'):
                WorkImage.objects.create(work=self.object, image=image)

        return response


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

  def get_queryset(self):
        queryset = super().get_queryset()
        # messages = Messages.objects.filter(receiver_id=self.request.user,reply=False).count()
        # print(messages)
        return queryset.filter(receiver_id=self.request.user)


class MessageCreate(CreateView):
  model = Messages
  fields = ['email','phoneNumber','budget','guestCount','eventType','eventDate','description']


  def form_valid(self,form):
    form.instance.sender =  self.request.user
    form.instance.receiver= User.objects.get(id=self.kwargs['workUser_id'])
    return super().form_valid(form)

class MessageReply(CreateView):
  model = Messages
  fields = ['email','phoneNumber','description']


  def form_valid(self,form):
    form.instance.sender =  self.request.user
    form.instance.receiver= User.objects.get(id=self.kwargs['workUser_id'])
    msg = Messages.objects.get(id=self.kwargs['message_id'])
    print(self.kwargs['message_id'])
    print(msg.reply)
    msg.reply='True'
    msg.save()
    return super().form_valid(form)

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
        vendorForm = VendorSignUp(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            if vendorForm.is_valid():
                profile = vendorForm.save(commit=False)
                profile.type = 'V'
                profile.user = user
                profile.save()
            elif profileForm.is_valid():
                profile = profileForm.save(commit=False)
                profile.user = user
                profile.save()
            else:
                error_message = 'Invalid Signup'
                print(form.errors)
                print(profileForm.errors)
                print(vendorForm.errors)
                return render(request, 'registration/signup.html', {'form': form, 'profileForm': profileForm, 'vendorForm': vendorForm, 'error_message': error_message})
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Signup'
            print(form.errors)

    form = CreateUserForm()
    profileForm = ProfileSignUp()
    vendorForm = VendorSignUp()

    context = {'form': form, 'profileForm': profileForm, 'vendorForm': vendorForm, 'error_message': error_message}
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
  work_users = User.objects.filter(id__in=work.users.all())
  # print(work_users)
  # workUser = User.objects.filter(id__in=work.users.all())
  # print('workUser',workUser)
  users_service=Profile.objects.filter(user_id__in=work_users.all())
  # print('userServes',users_service)


  # return render(request, 'works/detail.html', {'work': work, 'workUser':workUser,'userService':userService})
  return render(request, 'works/detail.html', {'work': work,' work_users': work_users,'users_service':users_service})



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





@login_required
def user_update(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        print(request.FILES)  # Check the structure of request.FILES
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()


            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            
            profile_form.save()
            return redirect('user_detail', user_id=user.id)
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'detail/user_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
        'profile': profile
    })
    
    


    
def customerSignup(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profileForm = CustomerSignUp(request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.type = 'C'
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Signup'
            print(form.errors)  
            print(profileForm.errors)  

    form = CreateUserForm()
    profileForm = CustomerSignUp()
    context = {'form': form, 'profileForm': profileForm, 'error_message': error_message}
    return render(request, 'registration/customer.html', context)




def vendorSignup(request):
    error_message = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profileForm = VendorSignUp (request.POST, request.FILES)
        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.type = 'V'
            profile.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Signup'
            print(form.errors) 
            print(profileForm.errors)  

    form = CreateUserForm()
    profileForm = VendorSignUp()
    context = {'form': form, 'profileForm': profileForm, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)




