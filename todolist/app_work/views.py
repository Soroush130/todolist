from django.shortcuts import render, redirect
from app_reminder.models import Reminder, MotivationalPhrases
from .forms import NewWork, TagForm
from .models import Tag, TypeWork, Work, Score
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from django.db.models import Q
import random
from .utils import ShowDaysOfMonth


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    date_now = datetime.now()
    date_end = date_now - timedelta(days=1)
    works = Work.objects.filter(user=request.user, start_work__range=[date_end, date_now]).order_by('-start_work')

    reminders = Reminder.objects.filter(date=datetime.now(),user=request.user)
    motivational_phrases_list = list(MotivationalPhrases.objects.all())
    if len(motivational_phrases_list) > 0:
        motivational_phrases = random.choice(motivational_phrases_list)
    else:
        motivational_phrases = None
    context = {
        "user": user,
        "works": works,
        "reminders": reminders,
        "motivational_phrases": motivational_phrases,
    }
    return render(request, 'app_work/work/home.html', context)


# add work to Todo list
@login_required(login_url='/accounts/login/')
def add_work(request):
    user = request.user
    works = Work.objects.filter(user=user).order_by('-start_work')
    tags = Tag.objects.filter(user=user)
    type_works = TypeWork.objects.all()

    if request.method == "POST":
        form = NewWork(request.POST)
        if form.is_valid():
            new_work = form.save(commit=False)
            new_work.user = request.user
            new_work.save()

            for type in form.cleaned_data['type_work']:
                new_work.type_work.add(type)

            for tag in form.cleaned_data['tag']:
                new_work.tag.add(tag)

            messages.success(request, 'فعالیت شما با موفقیت اضافه شد')
            return redirect('work:add_work')
        else:
            messages.error(request, 'مقادیر نامعتبر هستند')
    else:
        form = NewWork()

    context = {
        "form": form,
        "tags": tags,
        "type_works": type_works,
        "works": works,
    }
    return render(request, 'app_work/work/new-work.html', context)


# for chaeck work is complate or No (with ajax)
@login_required(login_url='/accounts/login/')
def check_work(request):
    if request.method == "GET":
        work_id = request.GET['work_id']
        work = Work.objects.get(id=work_id)
        if work.is_finished == False:
            work.is_finished = True
            work.save()
            response = {
                'is_finished': True,
            }
            return JsonResponse(response)
        elif work.is_finished == True:
            work.is_finished = False
            work.save()
            response = {
                'is_finished': False,
            }
            return JsonResponse(response)
    else:
        response = {
            'is_finished': 'method is not valid ( Method Valid : GET )',
        }
        return JsonResponse(response)


# func for delete work instance
@login_required(login_url='/accounts/login/')
def delete_work(request, work_id):
    url = request.META.get("HTTP_REFERER")
    try:
        Work.objects.get(id=work_id).delete()
        return redirect(url)
    except:
        return redirect(url)


###############
#     System Tag
###############

# add Tag
@login_required(login_url='/accounts/login/')
def tags(request):
    tag_list = Tag.objects.filter(user=request.user)
    tag_form = TagForm()
    return render(request, 'app_work/tag/tags.html', {'tags': tag_list, 'tag_form': tag_form, })


# create Tag
@login_required(login_url='/accounts/login/')
def add_tag(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.user = request.user
            new_tag.save()
            messages.success(request, 'تگ شما با موفقیت اضافه شد')
        else:
            messages.error(request, 'مقادیر نامعتبر هستند')

    return redirect(url)


# reporting Tag
@login_required(login_url='/accounts/login/')
def reporting_tag(request):
    tags = Tag.objects.filter(user=request.user)
    works = None

    if request.method == "POST":
        tag_list_input = request.POST.getlist('tags')
        tag_list_target = tags.filter(id__in=tag_list_input)

        for tag in tag_list_target:
            if tag.parent != None:
                if str(tag.parent.id) not in tag_list_input:
                    tag_list_input += str(tag.parent.id)

        works = Work.objects.filter(tag__in=tag_list_input, user=request.user).distinct()

    context = {
        'tags': tags,
        'works': works,
    }
    return render(request, 'app_work/tag/report-tag.html', context)


###############
#    Scoring system
###############
@login_required(login_url='/accounts/login/')
def scoring(request):
    works = None
    date = None
    score = None
    if request.method == "POST":
        type_date_day = request.POST.get('typeDateDay', None)
        type_date_month = request.POST.get('typeDateMonth', None)
        if type_date_day == 'on':
            day_user = request.POST.get('day', None)  # 2022-07-12, 2022-07-30, 2020-10-20
            date = day_user
            new_format = day_user.split('-')
            year = new_format[0]
            month = new_format[1]
            day = new_format[2]
            works = Work.objects.filter(user=request.user, start_work__year=year, start_work__month=month,
                                        start_work__day=day)
            score = Score.objects.filter(day=datetime(int(year), int(month), int(day))).first()
        elif type_date_month == 'on':
            month_user = request.POST.get('month', None)  # 2022-10, 2022-01, 2032-12
            date = month_user
            new_format = month_user.split('-')  # ['2022', '08']
            year = new_format[0]
            month = new_format[1]
            works = Work.objects.filter(user=request.user, start_work__year=year, start_work__month=month)
            score = Score.objects.filter(month=month_user).first()
    context = {
        'works': works,
        'score': score,
        'date': mark_safe(json.dumps(date)),
    }
    return render(request, 'app_work/score/scoring.html', context)

# ثبت امتیاز
@login_required(login_url='/accounts/login/')
def score_points(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        cd = request.POST
        day = cd['day']  # 2022-07-13
        month = cd['month']  # 2022-08
        rate = cd['rate']
        if day == '':
            is_exsist = Score.objects.filter(month=month).exists()
            if not is_exsist:
                Score.objects.create(user=request.user, month=month, rate=rate)
                messages.success(request, 'امتیاز شما ثبت شد')
            else:
                messages.error(request, 'برای این ماه قبل امتیاز ثبت کرده اید')
            return redirect(url)
        elif month == '':
            is_exsist = Score.objects.filter(day=day).exists()
            if not is_exsist:
                Score.objects.create(user=request.user, day=day, rate=rate)
                messages.success(request, 'امتیاز شما ثبت شد')
            else:
                messages.error(request, 'برای این روز قبل امتیاز ثبت کرده اید')
            return redirect(url)

@login_required(login_url='/accounts/login/')
def score_detail(request, score_id):
    context = {}
    try:
        score = Score.objects.get(id=score_id)
        if score.day:
            works = Work.objects.filter(user=request.user, start_work__year=score.day.year,
                                        start_work__month=score.day.month,
                                        start_work__day=score.day.day)
            context['works'] = works
        elif score.month:
            new_format = score.month.split('-')
            year = new_format[0]
            month = new_format[1]
            works = Work.objects.filter(user=request.user, start_work__year=year, start_work__month=month)
            context['works'] = works
        context['score'] = score
    except:
        pass

    return render(request, 'app_work/score/score-detail.html', context)

@login_required(login_url='/accounts/login/')
def score_edit(request, score_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        rate = request.POST['rate']
        score = Score.objects.get(id=score_id)
        score.rate = int(rate)
        score.save()
        return redirect(url)

@login_required(login_url='/accounts/login/')
def score_delete(request, score_id):
    try:
        score = Score.objects.get(id=score_id)
        score.delete()
        return redirect('work:scoring')
    except:
        # redirect page 404
        pass

######
@login_required(login_url='/accounts/login/')
def show_percent_work_daily_to_bar(request):
    context = {

    }
    return render(request, 'app_work/percent/show-percent-work-daily.html', context)

# Item 12 in project
@login_required(login_url='/accounts/login/')
def calc_percent_work_daily(request):
    if request.method == "GET":
        db_percent_finish_work = []
        db = {}
        value_date = request.GET['value_date']
        list_date_days_type_datetime, list_date_days_type_string = ShowDaysOfMonth(value_date)

        for index,day in enumerate(list_date_days_type_datetime):
            work = Work.objects.filter(user=request.user, start_work__year=day.year, start_work__month=day.month, start_work__day=day.day)
            count_all_work = work.count()
            count_is_finished_work = work.filter(is_finished=True).count()
            db[list_date_days_type_string[index]] = [count_all_work, count_is_finished_work]
            ##########################
            # calc percent works finished
            if count_all_work and count_is_finished_work > 0:
                percent = (count_is_finished_work/count_all_work) * 100
                db_percent_finish_work.append(percent)
            else:
                db_percent_finish_work.append(0)

        response = {
            'resulte': True,
            'list_date_days_type_string':list_date_days_type_string,
            'db':db,
            'db_percent_finish_work':db_percent_finish_work,
        }
        return JsonResponse(response)
    else:
        response = {
            'resulte': 'method is not valid ( Method Valid : GET )',
        }
        return JsonResponse(response)

# Item 11 in project
@login_required(login_url='/accounts/login/')
def show_percent_work_daily_to_circle(request):
    context = {

    }
    return render(request, 'app_work/percent/show-percent-work-daily-to-circle.html', context)


@login_required(login_url='/accounts/login/')
def calc_percent_to_circle(request):
    if request.method == "GET":
        value_date = request.GET['value_date']
        new_format = datetime.strptime(value_date, '%Y-%m-%d')
        works = Work.objects.filter(user=request.user, start_work__date=new_format)

        percents = []
        works_name = []

        for work in works:
            works_name.append(work.title)
            timedelta = work.end_work - work.start_work
            new_format = str(timedelta).split(':')
            hour = new_format[0]
            mint = new_format[1]
            
            calc_min = int(hour) * 60
            calc_min += int(mint)
            percent = calc_min * 0.0694444444444444
            percents.append(percent)

        response = {
            'resulte': True,
            'percents': percents,
            'works_name': works_name
        }
        return JsonResponse(response)
    else:
        response = {
            'resulte': 'method is not valid ( Method Valid : GET )',
        }
        return JsonResponse(response)