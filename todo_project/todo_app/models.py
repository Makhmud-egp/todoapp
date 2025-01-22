from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Not Started')  # Increase max_length to 12
    due_date = models.DateTimeField(null=True, blank=True)  # The due_date field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True)  # Added created_by field
    
    def __str__(self):
        return self.title

