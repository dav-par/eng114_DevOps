import requests
#print easting and northings for postcode
posts_codes_req = requests.get("https://api.postcodes.io/postcodes/SE120NB")
content_json = posts_codes_req.json()

print(content_json)
print()
print(type(content_json))
print()
print(content_json.keys())
print()

result = content_json['result']
print(result["eastings"], result["northings"])
print(result.get("eastings"), result.get("northings"))


