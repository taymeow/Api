import requests

BASE = "http://127.0.0.1:5000/"

# send get request to url
response = requests.get(BASE + "helloworld/tay/21")
# print response, .json so that it doesnt look like response object
print(response.json())