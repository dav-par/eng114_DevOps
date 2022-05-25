#use formatting to convert a number to currancy with 2 decimals

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, format_spec):
        if format_spec == "pounds":
            return str(f"£{(self.amount):.2f}")

        elif format_spec == "dollars":
            return str(f"${((self.amount*1.25)):.2f}")

    def add(self, a, b):
        return a + b

''' First go
    def __format__(self, format_spec):
        if format_spec == "pounds": #check format spec
            a = self.amount #assign value
            b = str(f"{a:.2f}") #convert to string with 2 decimals
            c = "£" + str(b) # add pound sign and print
            return c
'''


#user_amount = float(input(f"How much?"))

#print(user_amount)
'''
user_input = int(input(f"hello, how much do you have?\n"))

user_amount = Money(user_input)

print(f"in pounds that's: {user_amount:pounds}")

print(f"in dollars that's: {user_amount:dollars}")
'''