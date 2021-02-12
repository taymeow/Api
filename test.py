import requests

BASE = "http://127.0.0.1:500/"

# send get request to url
response = request.get(BASE + "helloworld")
# print response, .json so that it doesnt look like response object
print(response.json())