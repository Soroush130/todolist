from django.shortcuts import redirect, render
from .models import WaterDaily
from .forms import WaterDailyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def water_daily(request):
    count_glass_water = WaterDaily.objects.filter(user=request.user)
    form = WaterDailyForm()
    context = {
        'count_glass_water':count_glass_water,
        'form':form,
    }
    return render(request, 'app_water/water.html',context)

@login_required(login_url='/accounts/login/')
def add_galss_water(request):
    if request.method == "POST":
        form = WaterDailyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # print(cd) # {'count': 12, 'date': datetime.date(2022, 7, 1)}
            date = cd['date']
            is_exists = WaterDaily.objects.filter(date=date).exists()
            if not is_exists:
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()
                messages.success(request, 'با موفقیت ثبت شد')
            else:
                messages.error(request, 'این روز قبلا ثبت شده است')
            
    return redirect('water:water_daily')

@login_required(login_url='/accounts/login/')    
def delete_glass_water(request, day_id):
    try:
        WaterDaily.objects.get(id=day_id).delete()
        return redirect(request.META.get("HTTP_REFERER"))
    except:
        pass

@login_required(login_url='/accounts/login/')  
def edit_glass_water(request, day_id):
    if request.method == "POST":
        new_count = request.POST['count']
        day_glass_water = WaterDaily.objects.get(id=day_id)
        day_glass_water.count = new_count
        day_glass_water.save()
        messages.success(request, 'تغییرات اعمال شد')

    return redirect('water:water_daily')