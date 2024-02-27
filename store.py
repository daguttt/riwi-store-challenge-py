from json import load
from random import randrange

archivo_json = "products.json"

# with as sentence
with open(archivo_json, 'r') as file:
    data = load(file)

# Select a random product simulating an order
data_length = len(data)  # 31
random_product_index = randrange(0, data_length)

requested_product = data[random_product_index]


requested_product_str = "name={name};discount={discount};price={price};quantity={quantity}".format(
    name=requested_product["name"], discount=requested_product["discount"], price=requested_product["price"], quantity=requested_product["quantity"])

product_name = requested_product["name"]
product_price = requested_product["price"]
product_discount = requested_product["discount"]
product_quantity = requested_product["quantity"]

product_price_with_discount = int(
    product_price) * (100 - int(product_discount)) / 100
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
      price=product_price, price_with_discount=product_price_with_discount))

if int(requested_product["quantity"]) - 1 > 0:
    requested_product["quantity"] = int(requested_product["quantity"]) - 1
else:
    data.remove(requested_product)
