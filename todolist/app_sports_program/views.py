from django.shortcuts import redirect, render
from .models import Program, Item
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import ItemForm, ProgramForm
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def get_sport_programs(request):
    programs = Program.objects.filter(type='public')
    print(programs)
    context = {
        'programs':programs,
    }
    return render(request, 'app_sports_program/sport-program.html', context)

@login_required(login_url='/accounts/login/')
def add_sport_program(request):
    user = request.user
    if request.method == "GET":
        program_id = request.GET['program_id']
        program = Program.objects.get(id=int(program_id))
        if user not in program.user.all():
            program.user.add(user)
        else:
            program.user.remove(user)

        response = {
            'resulte': True
        }
        return JsonResponse(response)
    else:
        response = {
            'resulte': 'method is not valid ( Method Valid : GET )',
        }
        return JsonResponse(response)


@login_required(login_url='/accounts/login/')
def list_program_sport(request):
    programs = Program.objects.filter(user=request.user)
    context = {
        'programs':programs,
    }
    return render(request, 'app_sports_program/list-program-sport.html', context)
        

@login_required(login_url='/accounts/login/')
def delete_program_sport(request, program_id):

    url = request.META.get("HTTP_REFERER")
    user = request.user
    
    try:
        program = Program.objects.get(id=program_id)

        if program.type == 'private':
            if user in program.user.all():
                program.delete()
        else:
            program.user.remove(request.user)
        return redirect(url)
    except:
        return redirect('page_404')


@login_required(login_url='/accounts/login/')
def detail_program_sport(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
        context = {
            'program':program,
        }
        return render(request, 'app_sports_program/detail-program-sport.html',context)
    except:
        return redirect('page_404')
    
@login_required(login_url='/accounts/login/')
def new_customize_program(request):
    user = request.user
    items = Item.objects.filter(owner=user)
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            new_form.type = 'private'
            new_form.save()

            new_form.user.add(request.user)
            
            for i in form.cleaned_data['item']:
                new_form.item.add(i)
            
            messages.success(request,'برنامه شما با موفقیت ایجاد شد')
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            print('NOT')
    else:
        form = ProgramForm()
    context = {
        'items':items,
        'form':form,
    }
    return render(request, 'app_sports_program/new-customize-program.html',context)


@login_required(login_url='/accounts/login/')
def new_customize_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            messages.success(request, 'آیتم شما با موفقیت ثبت شد')
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, 'فرم نامعتبر است')
    else:
        pass
