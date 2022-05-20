import datetime


name = str(input("What is your name?\n")).capitalize()
age = int(input("How old are you?\n"))
#dob = datetime(input("What is your date of birth? DD/MM/YYYY\n"))
dob = input("What is your date of birth? DD/MM/YYYY\n")
score= float(input("What score did you get\n"))

print(f"{name} is {age} years old and born on {dob} and got {score:10%} to the nearest 10")

'''
name = input("What is your name?\n")
age = input("How old are you?\n")
dob = input("What is your date of birth?\n")

print(name + " is " + age + " born on " + dob)
print(type(45.j))
'''