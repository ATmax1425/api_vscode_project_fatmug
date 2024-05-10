import requests

json_ = {
    "id": 1,
    "po_number": "00001",
    "vendor": "001",
    "order_date": "2024-04-30",
    "delivery_date": "2024-05-09",
    "items": '{"product_name": "iPad Pro", "price": "99900.00"}',
    "quantity": 1,
    "status": "pending",
    "issue_date": "2024-04-30",
    "acknowledgment_date": "2024-04-05" #<-- added acknowledgment_date
}

response = requests.put("http://localhost:8000/api/purchase_orders/00001/", json=json_)

# print("json: ")
# print(response.json())
# print()
print("status_code: ")
print(response.status_code)