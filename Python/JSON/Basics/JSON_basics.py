import json

car_data= {"name": "telsa", "engine": "electric"}

print(type(car_data))

car_data_json_string = json.dumps(car_data)

print(type(car_data_json_string))
print(car_data_json_string)

with open("new_json_file.json", 'w') as jsonfile:
    json.dump(car_data, jsonfile)


with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile) #load makes the dictionary
    print(type(car))
    print(car["name"])
    print(car["engine"])

