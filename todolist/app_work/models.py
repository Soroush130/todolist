from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


class TypeWork(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children')
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    start_work = models.DateTimeField()
    end_work = models.DateTimeField()
    type_work = models.ManyToManyField(TypeWork, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True, default=None)
    is_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    
    def get_start_time(self):
        hour = self.start_work.hour
        minute = self.start_work.minute
        status = "AM" if hour<12 else "PM"
        result = f"{hour}:{minute} {status}"
        return result

    # get date => start_work.date
    def get_start_date(self):
        year = self.start_work.year
        month = self.start_work.month
        day = self.start_work.day
        result = f"{month}/{day}/{year}"
        return result

    def get_end_time(self):
        hour = self.end_work.hour
        minute = self.end_work.minute
        status = "AM" if hour<12 else "PM"
        result = f"{hour}:{minute} {status}"
        return result


    # get date => end_work.date
    def get_end_date(self):
        year = self.end_work.year
        month = self.end_work.month
        day = self.end_work.day
        result = f"{month}/{day}/{year}"
        return result


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField(blank=True, null=True)
    month = models.CharField(max_length=50, blank=True, null=True)
    rate = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
