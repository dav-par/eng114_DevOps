import requests

request_bbc = requests.get(("http://www.bbc.co.uk"))

print(request_bbc.status_code)