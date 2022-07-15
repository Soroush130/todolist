from urllib import request
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditeProfileForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        return redirect('/')


    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            email = cd['email']
            password = cd['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('account:login')
    else:
        form = RegisterForm()

    context = {
        'form':form,
    }

    return render(request, 'app_account/register.html', context)

def login_page(request):
    url = request.META.get("HTTP_REFERER")
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect(url)
    else:
        form = LoginForm()

    context = {
        "form": form, 
    }
    return render(request, 'app_account/login.html', context)

def log_out(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='/accounts/login/')
def edit_profile(request):

    profile = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = EditeProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات با موفقیت انجام شد')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'فرم نامعتبر است')
    else:
        form = EditeProfileForm(instance=profile)

    context = {
        'form':form,
        'profile':profile,
    }
    return render(request, 'app_account/edit-pofile.html', context)

