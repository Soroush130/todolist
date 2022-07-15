from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_from_user")    # sender
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_to_user")       # reciver
    body = models.TextField() 
    # date = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.from_user.username