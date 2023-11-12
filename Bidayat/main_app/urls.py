from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns=[
  path('',views.home, name='home'),
  path('about/',views.about,name='about'),


  # Message paths
  path('messages/',views.MessageList.as_view(),name='message_index'),
  path('messages/create',views.MessageCreate.as_view(),name='message_create'),
  path('messages/<int:pk>/update/',views.MessageUpdate.as_view(), name = 'message_update'),
  path('messages/<int:message_id>',views.Message_detail,name='message_detail'),
  path('messages/<int:pk>/delete',views.MessageDelete.as_view(),name='message_delete'),
  
  
  path('detail/user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
  path('accounts/signup/',views.signup,name='signup'),
  path('change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  
  
  path('categories/', views.categories_index, name='index'),
  path('categories/<int:category_id>', views.categories_detail, name='categorydetail'),

  path('categoryworks.html/<int:category_id>', views.works_category, name='categoryworks'),
  path('works/', views.works_index, name='workindex'),
  path('works/<int:work_id>', views.works_detail, name='workdetail'),
  path('works/create', views.WorkCreate.as_view(), name='works_create'),
  path('works/<int:pk>/update', views.WorkUpdate.as_view(), name='works_update'),
  path('works/<int:pk>/delete', views.WorkDelete.as_view(), name='works_delete'),
  
  # path('/', views.categories_base, name='index'),
]