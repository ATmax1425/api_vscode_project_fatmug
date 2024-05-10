import requests

json_ = {"vendor": "001"}

response = requests.get("http://localhost:8000/api/purchase_orders/", params=json_)

print("json: ")
print(response.json())
print()
print("status_code: ")
print(response.status_code)