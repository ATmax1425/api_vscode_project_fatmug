import requests

json_data = [
    {
        "po_number": "00001",
        "vendor": "001",
        "order_date": "2024-04-30",
        "delivery_date": "2024-05-09",
        "items": '{"product_name": "iPad Pro", "price": "99900.00"}',
        "quantity": 1,
        "status": "pending",
        "issue_date": "2024-04-30"
    },
    {
        "po_number": "00002",
        "vendor": "001",
        "order_date": "2024-05-03",
        "delivery_date": "2024-05-14",
        "items": '{"product_name": "iPad Pro", "price": "323600.00"}',
        "quantity": 3,
        "status": "pending",
        "issue_date": "2024-05-04"
    },
    {
        "po_number": "00003",
        "vendor": "002",
        "order_date": "2024-05-01",
        "delivery_date": "2024-05-10",
        "items": '{"product_name": "Galaxy S24 Ultra", "price": "159999.00"}',
        "quantity": 2,
        "status": "pending",
        "issue_date": "2024-05-04",
        "acknowledgment_date": "2024-05-05"
    },
    {
        "po_number": "00004",
        "vendor": "002",
        "order_date": "2024-04-05",
        "delivery_date": "2024-04-11",
        "items": '{"product_name": "Galaxy S24 Ultra", "price": "159999.00"}',
        "quantity": 1,
        "status": "completed",
        "quality_rating": 9,
        "issue_date": "2024-04-06",
        "acknowledgment_date": "2024-04-07"
    },
    {
        "po_number": "00005",
        "vendor": "002",
        "order_date": "2024-04-05",
        "delivery_date": "2024-04-15",
        "items": '{"product_name": "Galaxy S24 Ultra", "price": "159999.00"}',
        "quantity": 4,
        "status": "completed",
        "quality_rating": 7,
        "issue_date": "2024-04-06",
        "acknowledgment_date": "2024-04-07"
    },
    {
        "po_number": "00006",
        "vendor": "002",
        "order_date": "2024-04-01",
        "delivery_date": "2024-04-09",
        "items": '{"product_name": "Galaxy S24 Ultra", "price": "159999.00"}',
        "quantity": 4,
        "status": "completed",
        "quality_rating": 6,
        "issue_date": "2024-04-04",
        "acknowledgment_date": "2024-04-04"
    },
        {
        "po_number": "00007",
        "vendor": "003",
        "order_date": "2024-03-02",
        "delivery_date": "2024-03-10",
        "items": '{"product_name": "iPhone 17 Pro", "price": "254990.00"}',
        "quantity": 1,
        "status": "canceled",
        "quality_rating": 2,
        "issue_date": "2024-03-04",
        "acknowledgment_date": "2024-03-08"
    },
]

for json_ in json_data:
    response = requests.post("http://localhost:8000/api/purchase_orders/", json=json_)

print("json: ")
print(response.json())
print()
print("status_code: ")
print(response.status_code)