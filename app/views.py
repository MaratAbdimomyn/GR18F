from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import *

class UsersView(ListView):
    model = MyUsers
    template_name = 'home.html'
    context_object_name = 'one'

class AboutUser(DetailView):
    model = MyUsers
    template_name = 'about.html'
    context_object_name = 'ones'

class DeleteUser(DeleteView):
    model = MyUsers
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class CreateUser(CreateView):
    model = MyUsers
    template_name = 'create.html'
    fields = ['name', 'age', 'status']
    success_url = reverse_lazy('home')