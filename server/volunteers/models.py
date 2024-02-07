from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class AdminUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default='admin_username')
    email = models.EmailField(unique=True, default="admin@change.me")
    groups = models.ManyToManyField(Group, blank=True, related_name="adminuser_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="adminuser_permissions")
    password = models.CharField(max_length=128, default='admin_password')

    # Add these lines
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     related_name="adminuser_set",
    #     related_query_name="user",
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     related_name="adminuser_set",
    #     related_query_name="user",
    # )
class AnonymousUser(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()