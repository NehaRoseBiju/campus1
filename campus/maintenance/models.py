from django.db import models
from django.contrib.auth.models import User

class MaintenanceRequest(models.Model):
    PRIORITY = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]
    STATUS = [('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY, default='medium')
    status = models.CharField(max_length=15, choices=STATUS, default='pending')
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

