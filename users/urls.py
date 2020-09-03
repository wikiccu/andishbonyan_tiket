from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.login , name='login'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('tiket/', views.newtiket , name='new-tiket'),

]
