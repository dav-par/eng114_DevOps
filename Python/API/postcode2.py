import requests
import json

headers = {"Content-Type": "application/json"}
data = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})

r = requests.post(
    url="https://api.postcodes.io/postcodes/",
    headers=headers,
    data=data
)

print(r)
print(type(r))
print(r.content)
print()
print(r.json())
#print()
#print(r.json().get("error"))

#for each postcode, print postcode, region and parl
#for each postcode, print postcode, region and "parliamentary_constituency"
content_json = r.json()
print(content_json)
print(content_json.keys())
layer1 = content_json['result']
print("first step")
print(type(layer1))
print(layer1)
#layer2 = content_json['result']
print("second step")

for i in range(3):
    layer2 = layer1[i]
    layer3 = layer2["result"]
    a = layer3["postcode"]
    b = layer3["region"]
    c = layer3["parliamentary_constituency"]
    print(f"postcode: {a}, region: {b}, region: {c}")
