from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    
    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
            ("can_view", "Can view book"),
        ]

    def __str__(self):
        return self.title
