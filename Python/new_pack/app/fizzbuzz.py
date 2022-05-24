'''Fizzbuzz problem statement is very simple, you need to write a program that returns "fizz" if the number is a multiplier of 3, return "buzz" if its multiplier of 5, and return "fizzbuzz" if the number is divisible by both 3 and 5.'''


#program that:
#fizz for multiplier of 3
#buzz for multiplier of 5
#fizzbuzz if divisible by 3 and 5

#def self

#def function


for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0 and not i % 5 == 0:
        print("fizz")

    elif i % 5 == 0 and not i % 3 == 0:
        print("buzz")

    else: print(i)