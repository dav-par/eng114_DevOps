user_email = "bob@gmail.com"
user_pass = "Password123"



requesting_access = True

input_email = input(f"Please enter your email\n")

while requesting_access:
    if input_email == user_email:
        print(f"Hello {user_email}")
        input_pass = input(f"Please enter your password\n")

        while requesting_access:
            if input_pass == user_pass:
                print(f"Access granted {user_email}")
                requesting_access = False
            else: input_pass = input(f"Password incorrect, please check and try again\n")

    else:
        print(f"User not recognised")
        input_email = input(f"Please enter your email\n")


