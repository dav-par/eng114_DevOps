import requests

posts_codes_req = requests.get("https://api.postcodes.io/postcodes/SE120NB")
print()
print(posts_codes_req)
print()
print(posts_codes_req.status_code)
print()
print(posts_codes_req.headers)
print()
print(type(posts_codes_req.content))
print()
print(posts_codes_req.content)
print()
print(type(posts_codes_req.json()))
print()
print(posts_codes_req.json())
print()

r = requests.get("https://api.postcodes.io/postcodes/SE120N")
print(r, type(r))
print(r.status_code)

if r.status_code == 200:
    content = r.content
    print(content)