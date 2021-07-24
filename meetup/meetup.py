import calendar
from datetime import date

class MeetupDayException(Exception):
    pass

days = {"Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6}

days_r = {"1st" : range(1,8),
          "2nd" : range(8,15),
          "3rd" : range(15,22),
          "4th" : range(22,29),
          "5th" : range(29,32)}

def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar().monthdayscalendar(year, month)
    d=0
    if week in days_r.keys():
        for w in cal:
            if w[days[day_of_week]] in days_r[week]:
                d = w[days[day_of_week]]
                break
    else:
        if week == "last":
            cal.reverse()
        for w in cal:
            if week in ["first","last"] and w[days[day_of_week]] != 0:
                break
            elif week == "teenth" and w[days[day_of_week]] >= 13 and w[days[day_of_week]] < 20:
                break
        d = w[days[day_of_week]]
    if not d:
        raise MeetupDayException("There is no {} {} for the chosen month".format(week,day_of_week))
    return date(year,month,d)
