shopping_list = []


shopping_list.append("carrots")
shopping_list.append("carrots")
shopping_list.append("carrots")
shopping_list.append("carrots")

print(str(shopping_list) + "/n")

if shopping_list.count("carrots") > 3:
    print("you must love carrots!")
else:
    print("nice list")


mixture = [1, 2, 3, "one", "two", "three"]

print(mixture[1:3]) #prints index 1 and 2
print

#tuple, immutable
essentials = ("bread", "egg", "milk") #tupil

#essentials[0] = "ham" <<< this won't work, essentials is locked

#dictionaries, name is like the index
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lesson_names" : ["variable", "data_types", "set_up"]
}


print(student_1["stream"])

print(student_1.keys())

print()
#sets and frozen sets
car_parts = {"wheels", "doors", "exhaust"} #random order
car_parts.add("windows") #.discard
print(car_parts)
print()

#frozen set
x = frozenset([1, 2, 3])  #immutable set
print(x)