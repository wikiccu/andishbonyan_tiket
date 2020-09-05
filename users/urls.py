from django.urls import path
from . import views 

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('login/', views.login , name='login'),
    path('tiket/', views.newtiket , name='new-tiket'),
]
