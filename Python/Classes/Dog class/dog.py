class Dog:

    breed = "canine"

    def bark(self):
        return "woof"


fido = Dog()
lassie = Dog()
fido.breed = "Jack russel"
lassie.breed = "Super dog"


print(type(fido))
print(fido.breed)
print(fido.bark())


print(type(lassie))
print(lassie.breed)
print(lassie.bark())

freddy = Dog()

print(type(freddy))
print(freddy.breed)
print(freddy.bark())