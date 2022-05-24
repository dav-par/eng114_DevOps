#use formatting to convert a number to currancy with 2 decimals

class Money:

    def __init__(self, amount):
        self.amount = amount

    def __format__(self, format_spec):
        if format_spec == "pounds":
            a = self.amount
            b = str(f"{a:.2f}")
            c = "£" + str(b)
            return c



#user_amount = float(input(f"How much?"))

#print(user_amount)

user_input = 200.223 #input(f"hello, how much do you have?\n")


user_amount = Money(user_input)

print(f"in pounds that's: {user_amount:pounds}")

print(f"in dollars that's: {user_amount:pounds}")
