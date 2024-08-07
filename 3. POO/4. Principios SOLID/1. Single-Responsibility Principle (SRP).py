"""
Principio de Responsabilidad Unica:
Una clase debe tener solo una funcionalidad. 
"""
class Order:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.payed = False
        self.total = price * quantity

class Warehouse:
    def __init__(self):
        self.storage = {
            "Cookies" : 420,
            "Magic Powder" : 100,
        }
    def check_stock(self, order):
        for element, stock in self.storage.items():
            if order.product == element and order.quantity <= stock:
                return True
            else:
                return False
            
    def __str__(self):
        return f"{self.storage}"
            
class Payment:
    def pay(self, order, warehouse):
        print(f"Product Name : {order.product}\nQuantity: {order.quantity}\nTotal Price ${order.total} MIAUSD")
        get_money = int(input("Insert money: "))
        if get_money >= order.total:
            change = get_money - order.total
            if warehouse.check_stock(order):
                warehouse.storage[order.product] -= order.quantity
                order.payed = True
                print(f"Change :{change}\nProduct payed: {order.payed} \nThank you for your order!! Come soon...")
            else:
                print(f"Product payed: {order.payed} \nSorry, We don't have stock of this item")
        else:
            print("Sorry, You don't have enought money! Go get a fucking job...")

product_1 = Order("Cookies", 420, 2)
warehouse = Warehouse()
payment = Payment()
payment.pay(product_1, warehouse)

print(warehouse)

product_2 = Order("Cookies", 10000, 2) #MORE COOKIES >:3
payment.pay(product_2, warehouse) #NO COOKIES???!!!
print(warehouse)

#Each class have a single functionality