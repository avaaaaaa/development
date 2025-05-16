import csv


user_list = [
    {"name": "john", "password": "john1", "is_admin": True},
    {"name": "mike", "password": "mike1", "is_admin": False},
    {"name": "bruce", "password": "bruce1", "is_admin": False},
]

with open("output.csv", "w", newline="") as f:
    fields = ["name", "password", "is_admin"]
    writer = csv.DictWriter(f, fieldnames=fields)

    writer.writeheader()  # write fields
    for user in user_list:
        writer.writerow(user)  # write user data according to fields
