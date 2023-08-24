from django.db import models
from django.urls import reverse_lazy, reverse

class MyUsers(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('about', args=[str(self.id)])