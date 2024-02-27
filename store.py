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
random_product_index = randrange(0, data_length)

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
requested_product_str = ";".join(product_formatted_entries)
entry_str_list = requested_product_str.split(';')
# Extract order info
recreated_product = {}
for entry_str in entry_str_list:
    key = entry_str.split('=')[0]
    value = entry_str.split('=')[1]
    recreated_product.setdefault(key, value)

print(recreated_product)
product_name = recreated_product["name"]
product_price = recreated_product["price"]
product_discount = recreated_product["discount"]
product_quantity = recreated_product["quantity"]

# print(product_name, product_price, product_discount, product_quantity)
product_price_with_discount = int(
    product_price) * (100 - int(product_discount)) / 100
print(product_price_with_discount)
request_total_price_with_discount = product_price_with_discount * \
    int(product_quantity)
request_total_price = int(product_price) * int(product_quantity)


receipt_template = """
--- Tu factura ---

Producto: {name}
Descuento: {discount}%
Precio Original: {price}
Precio Con Descuento: {price_with_discount}
"""
print(receipt_template.format(name=product_name, discount=product_discount,
      price=request_total_price, price_with_discount=request_total_price_with_discount))

if int(recreated_product["quantity"]) - 1 > 0:
    recreated_product["quantity"] = int(recreated_product["quantity"]) - 1
else:
    data.remove(requested_product)
