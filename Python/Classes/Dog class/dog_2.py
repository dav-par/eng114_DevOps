class Dog:

    breed = "canine"

    def __init__(self ,name, colour):
        self.breed = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof!"

fido = Dog("Fido", "brown")
fido.breed = "Jack russel"

print(f"{fido.name} is a {fido.colour} {fido.breed}. {fido.name} goes {fido.bark()}")

