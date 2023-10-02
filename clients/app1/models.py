from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

# class Project(models.Model):
#     project_name = models.CharField(max_length=255)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     users = models.ManyToManyField(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    # Add related_name for created_by
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    
    # Add related_name for users
    users = models.ManyToManyField(User, related_name='assigned_projects')
    
    created_at = models.DateTimeField(auto_now_add=True)
