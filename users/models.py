from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    # Кандидат, HR-менеджер, Администратор
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

