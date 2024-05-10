import requests

response = requests.get("http://localhost:8000/api/vendors/")

print("json: ")
print(response.json())
print()
print("status_code: ")
print(response.status_code)