from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('listing/<int:listing_id>', views.listing, name='listing'),
    path('tasks/<int:listing_id>', views.tasksListing, name='taskslisting'),
    #path('tasks/<int:tiketid>', views.tiketListing, name='tiketListing'),
    path('login/', views.login , name='login'),
    path('tasks/', views.tasks , name='tasks'),
]
