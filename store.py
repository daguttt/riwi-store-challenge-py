from json import load
from random import randrange

archivo_json = "products.json"

# 1.
with open(archivo_json, 'r') as file:
    data = load(file)

# 2. Select a random product simulating an order
data_length = len(data)  # 31
random_product_index = randrange(0, data_length)

requested_product = data[random_product_index]

# 3.
requested_product_str = "name={name};discount={discount};price={price};quantity={quantity}".format(
    name=requested_product["name"], discount=requested_product["discount"], price=requested_product["price"], quantity=requested_product["quantity"])

entry_str_list = requested_product_str.split(';')

# 4.
# product name
product_name_key = entry_str_list[0].split('=')[0]
product_name_value = entry_str_list[0].split('=')[1]

# product discount
product_discount_key = entry_str_list[1].split('=')[0]
product_discount_value = entry_str_list[1].split('=')[1]

# product price
product_price_key = entry_str_list[2].split('=')[0]
product_price_value = entry_str_list[2].split('=')[1]

# product quantity
product_quantity_key = entry_str_list[3].split('=')[0]
product_quantity_value = entry_str_list[3].split('=')[1]

recreated_product = {
    product_name_key: product_name_value,
    product_discount_key: product_discount_value,
    product_price_key: product_price_value,
    product_quantity_key: product_quantity_value
}

# 5.
product_price_with_discount = int(
    recreated_product["price"]) * (100 - int(recreated_product["discount"])) / 100

# 6.
request_total_price_with_discount = product_price_with_discount * \
    int(recreated_product["price"])
request_total_price = int(
    recreated_product["price"]) * int(recreated_product["quantity"])

# 7.
receipt_template = """
--- Tu factura ---

Producto: {name}
Descuento: {discount}%
Precio Original: {price}
Precio Con Descuento: {price_with_discount}
"""

print(receipt_template.format(name=recreated_product["name"], discount=recreated_product["discount"],
      price=recreated_product["price"], price_with_discount=product_price_with_discount))

# 8.
data[random_product_index]["quantity"] -= 1
if data[random_product_index]["quantity"] == 0:
    data.pop(random_product_index)

print(data[random_product_index])
