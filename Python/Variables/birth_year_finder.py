from datetime import date

def what_year():
    name = str(input("What is your name?\n")).capitalize()
    age = int(input("How old are you?\n"))
    current_year = (date.today()).year
    year = current_year - age
    print(f"{name}! you were born in {year}")

what_year()

