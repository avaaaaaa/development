class Store:
    def __init__(self, name, sales_tax=.088, products=[]):
        self.name = name
        self.sales_tax = sales_tax
        self.products = products
    def add_product(self, product):
        self.products.append(product)
    def delete_product(self, product):
        try:
            self.products.remove(product)
        except ValueError:
            print(product.name, "is not found in product list")

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name
        self.products = []
    def buy_product(self, product):
        self.products.append(product)
    def get_receipt(self, store):
        total_price = 0
        description = "Purchase by " + self.name.upper() + "\n"
        while self.products:
            product = self.products.pop()
            total_price += product.price
            description += (product.description +
                            "\n   Cost: " +
                            str(product.price) + "\n")
        description += ("TOTAL COST\n" + 
                        f"   Price: {total_price}" +
                        f"\n   Tax(%{store.sales_tax * 100}): {total_price * store.sales_tax}" +
                        f"\n   Total: {total_price + total_price * store.sales_tax}"
                        )
        
        return description


lovely_loveseat = Product(
    "Lovely Loveseat",
    "Lovely Loveseat. Tufted polyester blend on wood. " \
        "32 inches high x 40 inches wide x 30 inches deep. Red or white.",
    254.00
)

stylish_settee = Product(
    "Stylish Settee",
    "Stylish Settee. Faux leather on birch. " \
        "29.50 inches high x 54.75 inches wide x 28 inches deep. Black.",
    180.50
)

luxurious_lamp = Product(
    "Luxurious Lamp",
    "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.",
    52.15
)

store = Store("Lovely Loveseats for Neat Suites")
store.add_product(lovely_loveseat)
store.add_product(stylish_settee)
store.add_product(luxurious_lamp)

customer_john = Customer("John")
customer_john.buy_product(lovely_loveseat)
customer_john.buy_product(luxurious_lamp)

receipt = customer_john.get_receipt(store)
print(receipt)