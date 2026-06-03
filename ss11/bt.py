users= [
    {"name": "Bảo", "age": 18},
    {"name": "Nguyên", "age": 18},
    {"name": "Thắng", "age": 18}
]
for user in users:
    print(f"name : {user["name"]}, age : {user["age"]}")
users.append("gender")