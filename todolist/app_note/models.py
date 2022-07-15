from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nots')
    title = models.CharField(max_length=300)
    body = models.TextField()
    # date = models.DateTimeField(blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True, default=None)

    created_note = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title