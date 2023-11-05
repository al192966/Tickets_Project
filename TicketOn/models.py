from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class eventos(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.TextField(blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + '- de ' + self.user.username