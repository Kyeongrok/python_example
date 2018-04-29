list = [
    {"name":"kyeongrok", "age":32},
    {"name":"kyeongrok2", "age":33},
    {"name":"kyeongrok3", "age":34}
]

filtered_list = []
for user in list:
    if user['age'] > 33:
        filtered_list.append(user)

print(filtered_list)