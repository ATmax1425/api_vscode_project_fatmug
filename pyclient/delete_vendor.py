import requests

response = requests.delete("http://localhost:8000/api/vendors/006/")

# print("json: ")
# print(response.json())
# print()
print("status_code: ")
print(response.status_code)