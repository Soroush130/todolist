import calendar
import datetime

def find_date_days_in_month(firstDayOfMonth, lastDayOfMonth):
    year_now = firstDayOfMonth.year
    month_now = firstDayOfMonth.month
    month_now = f'0{month_now}' if month_now < 10 else month_now
    date_list = []
    step = 15

    for day in range(firstDayOfMonth.day,step+1):
        day = f'0{day}' if day < 10 else day
        format = f'{year_now}-{month_now}-{day}'
        date_list.append(format)


    for day in range(step+1, lastDayOfMonth.day+1):
        day = f'0{day}' if day < 10 else day
        format = f'{year_now}-{month_now}-{day}'
        date_list.append(format)

    return date_list

def change_format_str_to_datetime(date_string):
    dateobj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return dateobj

def ShowDaysOfMonth(date):
    now_format = date.split('-')
    year = int(now_format[0])
    month = int(now_format[1])
    # count days in month
    # daysInMonth= calendar.monthrange(year, month)[1]
    # get first day in month
    firstDayOfMonth = datetime.date(year, month, 1) 
    # get last day in month
    lastDayOfMonth = datetime.date(year, month, calendar.monthrange(year, month)[1])

    result_old = find_date_days_in_month(firstDayOfMonth,lastDayOfMonth,)  
    result = list(map(change_format_str_to_datetime, result_old))
    return result, result_old