from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path(r'$', views.dashboard ),
    path('<int:listing_id>', views.listing, name='listing'),
    path('login/', views.login , name='login'),
    path('tasks/', views.tasks , name='tasks'),
]
