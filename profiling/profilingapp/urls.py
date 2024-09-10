from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.profile_create, name='profile_create'),
    path('update/<int:id>/', views.profile_edit, name='profile_edit'),
    path('delete/<int:id>/', views.profile_delete, name='profile_delete'),
    path('detail/<int:id>/', views.profile_detail, name='profile_detail'),
]