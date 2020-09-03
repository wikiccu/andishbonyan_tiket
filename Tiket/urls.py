from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("users.urls")),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
]
