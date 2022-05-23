list_data = [1, 2, 3, 4, 5]
embedded_list = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "money", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(num*2)


for data in embedded_list:
    print(data)
    for data2 in data:
        print(f"internal data value: {data2}")

print(f"dict data\n")
for item in dict_data.values():
    print(item)
    for embeded_value in item.values():
        print(embeded_value)

print("identifier\n")
for item in dict_data.values():
    print(item['money'])

