#inventory management system
class Product:
    products = {}

    def __init__(self, name, price, quantity, id):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def add_product(cls, product):
        cls.products[product.id] = product
        print(f"\nProduct '{product.name}' added to inventory.\n")

    def update_quantity(self, quantity, id):
        if self.id == id:
            self.quantity += quantity
            print(f"Quantity of '{self.name}' updated to {self.quantity}.")

    def update_price(self, price, id):
        if self.id == id:
            self.price = price
            print(f"Price of '{self.name}' updated to ${self.price:.2f}.")

    def display_product(self):
        print(f"Product ID: {self.id}")
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")

    @classmethod
    def display_products(cls):
        if not cls.products:
            print("Inventory is empty.")
            return

        print("Inventory:")
        for product in cls.products.values():
            product.display_product()
            print()

    @classmethod
    def generate_inventory_report(cls):
        if not cls.products:
            return "Inventory is empty."

        lines = [
            "Inventory Report",
            f"{'ID':<6}{'Product':<22}{'Price':>10}{'Quantity':>12}{'Stock Value':>15}",
            "-" * 65,
        ]

        total_quantity = 0
        total_value = 0
        for product in cls.products.values():
            stock_value = product.price * product.quantity
            total_quantity += product.quantity
            total_value += stock_value
            lines.append(
                f"{product.id:<6}{product.name:<22}"
                f"${product.price:>9.2f}{product.quantity:>12}"
                f"${stock_value:>14.2f}"
            )

        lines.extend(
            [
                "-" * 65,
                f"Products: {len(cls.products)}",
                f"Total units: {total_quantity}",
                f"Total inventory value: ${total_value:.2f}",
            ]
        )
        return "\n".join(lines)
    @classmethod
    def search_product(cls, name):
        for product in cls.products.values():
            if product.name.lower() == name.lower():
                print(f"Product found: {product.name}, Price: ${product.price:.2f}, Quantity: {product.quantity}")
                return
        print(f"Product '{name}' not found in inventory.")