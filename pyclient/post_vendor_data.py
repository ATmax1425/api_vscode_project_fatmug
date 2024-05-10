import requests

json_data = [
    {
        "name": "raj malhotra",
        "contact_details": "9853847592",
        "address": "Baner, Pune, Maharashtra, India",
        "vendor_code": "001",
    },
    {
        "name": "Cherie R Fowler",
        "contact_details": "205-641-7661",
        "address": "2239 Broad Street Birmingham, Alabama(AL), 35209",
        "vendor_code": "002",
    },
    {
        "name": "James D Franklin",
        "contact_details": "201-600-6589",
        "address": "193 Moonlight Drive Maple Shade, New Jersey(NJ), 08052",
        "vendor_code": "003",
    },
    {
        "name": "Robert K Jones",
        "contact_details": "412-526-0001",
        "address": "1152 Beechwood Drive Pittsburgh, Pennsylvania(PA), 15213",
        "vendor_code": "004",
    },
    {
        "name": "Catherine A Christensen",
        "contact_details": "425-780-7725",
        "address": "2144 Honeysuckle Lane Bothell, Washington(WA), 98011",
        "vendor_code": "005",
    },
    {
        "name": "Zoe S Guerrero",
        "contact_details": "612-388-3980",
        "address": "3236 Bryan Avenue Eagan, Minnesota(MN), 55121",
        "vendor_code": "006",
    }
]

for json_ in json_data:
    response = requests.post("http://localhost:8000/api/vendors/", json=json_)

print("json: ")
print(response.json())
print()
print("status_code: ")
print(response.status_code)