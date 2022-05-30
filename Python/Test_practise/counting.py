

string = '$100 $200 $300'
# print(string.count("$"))
# print(string.count("$", 5, 10))
# print(string.count("$", 5))
#
# for a in string: print(a)

for a in string: print(f"{string.index(a)} = {a}")