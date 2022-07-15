from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField(default=0, blank=True,null=True)
    repeat_count = models.CharField(max_length=255, blank=True, default='0')

    def __str__(self) -> str:
        return self.title



class Program(models.Model):
    TYPE_PROGRAM = (
        ('public', 'PUBLIC'),
        ('private', 'PRIVATE')
    )
    type = models.CharField(max_length=10, choices=TYPE_PROGRAM, default='public')
    titel = models.CharField(max_length=255)
    item = models.ManyToManyField(Item, related_name='programs_item')
    user = models.ManyToManyField(User, related_name='programs_user', blank=True)

    def __str__(self) -> str:
        return self.titel