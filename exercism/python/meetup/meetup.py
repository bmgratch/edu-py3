import datetime as dt

addwk = dt.timedelta(days=7)

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
          'Friday', 'Saturday', 'Sunday'] #for getting day_of_week
    
    start = dt.date(year, month, 1)
    newday = go_to_wd(start, wd.index(day_of_week))
    
    if week[0] == 't':
        return(is_teenth(newday))
    if week[0] == 'l':
        return(is_last(newday))
    return(is_number(newday, int(week[0])))

def is_number(date, target):
    counter = 1
    mo = date.month
    while counter < target:
        date += addwk
        counter += 1
    if mo != date.month:
        raise MeetupDayException('This day does not exist.')
    return date

def is_teenth(date):
    while date.day < 13:
        date += addwk
    return date

def is_last(date):
    next_mo = date + dt.timedelta(days=31)
    while (date + addwk).month != next_mo.month:
        print(date.strftime("%Y, %B, %d %A"))
        date += addwk
    return date

def go_to_wd(date, target):
    while date.weekday() != target:
        date += dt.timedelta(days=1)
    return date
