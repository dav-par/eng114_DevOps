class Dog:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old Dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A  {self.age * 7} dog years old"
    else:
        return self.__str()

fido = Dog(5)
print(f"{fido}")
print(f"{fido:dog}")