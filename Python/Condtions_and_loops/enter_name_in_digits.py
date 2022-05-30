user_prompt = True

while user_prompt:
    age = input("What is your age?\n")
    if age.isdigit():
        user_prompt = False
    else:
        print("Plese provide your age in digits")

print(f"Your age is {age}")