data = [
    {"id": 10, "user": "Bob"},
    {"id": 11, "user": "Misha"},
    {"id": 12, "user": "Anton"},
    {"id": 10, "user": "Bob"},
    {"id": 11, "user": "Misha"},
]

# unique_data = []
# for i_dict in data:
#     data_exists = False
#     for unique_dict in unique_data:
#         if unique_dict['id'] == i_dict['id']:
#             data_exists = True
#             break
#     if not data_exists:
#         unique_data.append(i_dict)

# print(unique_data)

unique_data = {i_dict["id"]: i_dict for i_dict in data}
print(unique_data.values())
