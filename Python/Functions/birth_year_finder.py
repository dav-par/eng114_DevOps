import datetime
from datetime import date

def what_year():
    name = str(input("What is your name?\n")).capitalize()
    age = int(input("How old are you?\n"))
    b_month = int(input("what month were you born in? (Jan = 1 etc)\n"))
    b_day = int(input("what day of the month were you born in?\n"))
    current_year = (date.today()).year

    year = current_year - age
    if b_month >= int((date.today()).month):
        if b_day <= int((date.today()).day):
            year -= 1
    print(f"{name}! you were probably born in the year {year}.")
    bday = datetime.date(year, b_month, b_day)
    datetime.timedelta(date.today(), bday)
    print(bday)
    days = date.today() - bday
    print(days)
    #hours = datetime(days)
    #print(hours)

what_year()



#expanded task, how many hours have you been alive?