from django.urls import path
from . import views

urlpatterns=[
  path('',views.home, name='home'),
  path('about/',views.about,name='about'),
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