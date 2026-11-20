from pathlib import Path

from oops2 import *

product = Product("Laptop", 1000, 10, 1)
pro = Product("Smartphone", 500, 20, 2)
pro2 = Product("Tablet", 300, 15, 3)

Product.add_product(product)
Product.add_product(pro)
Product.add_product(pro2)

report = Product.generate_inventory_report()
report_path = Path(__file__).with_name("inventory_report.txt")
report_path.write_text(report + "\n", encoding="utf-8")
print(f"Inventory report saved to {report_path}")
Product.search_product("Tablet")

