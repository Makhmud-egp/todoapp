from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    ), default='Not Started')

    def __str__(self):
        return self.title
