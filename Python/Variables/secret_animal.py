#collect input
name = str(input("what is your name?\n"))
height = int(input("what is your height?\n"))
favourite_colour = str(input("what is your favourite colour?\n"))
secret_animal = str(input("what is your secret animal?\n"))

#set variables
animal_first = secret_animal[0]
animal_last = secret_animal[-1]
animal_charnum = len(secret_animal)

#welcome message
print(f"{name}! you're {height} tall!")

#animal letters
print(f"The first letter of your animal is {animal_first}, the last letter is {animal_last}.")

#animal name length
print(f"Your animals name is {animal_charnum} letters long.")

#extra question
guess = ""
guess = input("Can you guess your secret animal?\n")
if guess == secret_animal: print("You got it right, well done! :)")
else: print("That's not quite right but good try!")

#close
print()
print("Thank you for playing")