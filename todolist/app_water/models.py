from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class WaterDaily(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    date = models.DateField()

    def __str__(self) -> str:
        return self.user.username
    
    # def save(self, *args, **kwargs):
    #     result = WaterDaily.objects.filter(date=self.date).exists()
    #     if not result:
    #         super(WaterDaily, self).save(*args, **kwargs)
    #     else:
    #         # raise ValueError('Some has been recorded on this date')
    #         pass