users = {
    "bob@gmail.com": "Password123",
    "fred@gmail.com": "Password1234"
}

requesting_access = True

input_email = input(f"Please enter your email\n")

while requesting_access:
    if input_email in users:
        print(f"Hello {input_email}")
        input_pass = input(f"Please enter your password\n")

        while requesting_access:
            if input_pass == users[input_email]:
                print(f"Access granted {input_email}")
                requesting_access = False
            else: input_pass = input(f"Password incorrect, please check and try again\n")

    else:
        print(f"User not recognised")
        input_email = input(f"Please enter your email\n")


