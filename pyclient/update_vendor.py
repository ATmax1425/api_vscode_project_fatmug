import requests

json_ = {
    "id": 1,
    "name": "Raj K Malhotra", #<-- updated name
    "contact_details": "985-384-7592", #<-- updated contact_details
    "address": "Baner, Pune, Maharashtra, India",
    "vendor_code": "001",
    "on_time_delivery_rate": 0.0,
    "quality_rating_avg": 0.0,
    "average_response_time": 0.0,
    "fulfillment_rate": 0.0
}

response = requests.put("http://localhost:8000/api/vendors/001/", json=json_)

# print("json: ")
# print(response.json())
# print()
print("status_code: ")
print(response.status_code)