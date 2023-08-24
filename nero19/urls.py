from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UsersView.as_view(), name='home'),
    path('about/<int:pk>', AboutUser.as_view(), name='about'),
    path('delete/<int:pk>', DeleteUser.as_view(), name='delete'),
    path('create', CreateUser.as_view(), name='create')
]