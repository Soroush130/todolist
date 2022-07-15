from django.shortcuts import render, redirect
from .models import Reminder
from .forms import ReminderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(login_url='/accounts/login/')
def reminders(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('-date')
    form = ReminderForm()
    context = {
        'reminders': reminders,
        'form': form,
        'date_now':datetime.now(),
    }
    return render(request, 'app_reminder/reminders.html', context)


@login_required(login_url='/accounts/login/')
def add_reminder(request):
    if request.method == "POST":
        form = ReminderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'یادآوری جدید ثبت شد')
            return redirect('reminder:reminders')
        else:
            messages.error(request, 'مقادیر فرم به درستی وارد نشده')
            return redirect('reminder:reminders')
