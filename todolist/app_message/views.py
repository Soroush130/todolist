from django.shortcuts import redirect, render
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from datetime import datetime
from django.contrib import messages

User = get_user_model()

@login_required(login_url='/accounts/login/')
def message_list(request):
    date_today = datetime.today()
    date = date_today.date()
    time = date_today.time()
    message_list = Message.objects.filter(to_user=request.user, date__lte=date, time__lte=time)
    context = {
        "messages":message_list,
    }
    return render(request, 'app_message/messages.html',context)


@login_required(login_url='/accounts/login/')
def send_message(request):
    url = request.META.get("HTTP_REFERER")
    users = User.objects.exclude(username=request.user.username)
    message_sent = Message.objects.filter(from_user=request.user)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.from_user = request.user
            new_form.save()

            messages.success(request,'Send message from user')
            return redirect(url)
    else:
        form = MessageForm()
    context = {
        "form":form,
        "users":users,
        "message_sent":message_sent,
    }
    return render(request, 'app_message/send-message.html', context)

@login_required(login_url='/accounts/login/')
def delete_messsage(request, message_id):
    url = request.META.get("HTTP_REFERER")
    try:
        Message.objects.get(id=message_id).delete()
        return redirect(url)
    except:
        pass