total =0

def add_two_values(a, b):
    return a + b

def minus_two_values(a, b):
    return a - b

def times_two_values(a, b):
    return a * b

def divide_two_values(a: int,b: int) -> float:
        return a / b

def sum_all(*args):
    return sum(args)

def minus_all():
    first = int(input(f"What value do you want to minus from?\n"))
    to_remove = input(f"What values do you want to minus? (separate them with a comma)\n").split(",")
    print(type(to_remove))
    print(to_remove)
    print([x for x in to_remove])

print(add_two_values(2, 3))

print(minus_two_values(5,6))

print(times_two_values(634, 534))

print(divide_two_values(4345, 434))

print(sum_all(3, 3, 5, 6, 3))

minus_all()

