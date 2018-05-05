import requests

url = "https://api.hanbitco-qa.com/v1/auth/login"
headers = {'content-type':'application/json'}
data = {"email":"james+3072@plutusds.com", "password":"1234@Qwer"}
req = requests.post(url=url, headers=headers,  json=data)

print(req.url)
print(req.status_code)
print(req.json())
print(req.reason)
