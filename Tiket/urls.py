from django.contrib import admin
from django.urls import path
from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.home),
]
