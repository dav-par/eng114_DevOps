
example_text = "This is a great sentence!, look at all the words it has!"

print(example_text[7:])
print(example_text[:-3])
print(example_text[2:-13])

print(example_text.count("e"))
print(example_text.upper())
print(example_text.lower())


score = 16
max_score = 26
print(f"you scored {score/max_score:%}")
print(f"you scored {score/max_score:.2%}")
print(f"you scored {score/max_score:.0%}")
