users = []

def get_user_info():
    i = len(users)
    name= str(input("What is your name?\n "string))
    age = int(input("How old are you?\n"))
    dob = datetime(input("What is your date of birth?\n"))
    users.append([name, age, dob])
    print(f"{name} is {age} years old and born on {dob}")

def run_program():
    if input("Do you want to add a user?\n").lower() == "yes" or input == "y":
        get_user_info()
    else: print("Thank you for considering joining our list")

run_program()