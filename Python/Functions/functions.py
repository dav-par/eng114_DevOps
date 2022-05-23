def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)


multi_args(5, 4, 3, 2, 2, True, "fred")

def greeting(name: str):
    print("Hello, my name is " + name)


greeting("bob")