items = [
    {
        "product" : "t-shirt",
        "price" : 100
    },
    {
        "product" : "pants",
        "price" : 200
    },
    {
        "product" : "boots",
        "price" : 300
    }
]
prices = list(map(lambda x: x["price"], items))
print(prices)

tax = 0.19

def add_taxes(item):
    new_item = item.copy() #Copia para preservar los valores del array anterior
    new_item["taxes"] = new_item["price"] * tax
    return new_item

new_items = list(map(add_taxes, items))
print("New items:", new_items)
print("Old items:", items)