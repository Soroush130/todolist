from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class MotivationalPhrases(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=400)

    def __str__(self) -> str:
        return self.title
