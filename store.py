from json import load
from random import randrange

archivo_json = "products.json"

# with as sentence
with open(archivo_json, 'r') as file:
    data = load(file)
    # print(data)

# Select a random product simulating an order
data_length = len(data)  # 31
# print(data_length)
#                                    #             🔽 To make sure we count select the last item
random_product_index = randrange(0, data_length + 1)

# print(selected_product_index)
requested_product = data[random_product_index]
# print(random_selected_product)

# dict -> str => key=value;
# 3. Format requested product into a str
#                                          0                 1
# [("name", "smartwatch"), ('discount', 30)]
#     name=smartwatch
product_entries = list(requested_product.items())
product_formatted_entries = []  # empty
for entry in product_entries:
    key = entry[0]
    value = entry[1]
    formatted_entry = f"{key}={value}"  # 'key=value'
    product_formatted_entries.append(formatted_entry)

# product_formatted_entries = ["name=smartwatch", "discount=30"]

formatted_product_str = ";".join(product_formatted_entries)
print(formatted_product_str)
