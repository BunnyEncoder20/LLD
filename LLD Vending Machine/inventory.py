from product import Product
from collections import defaultdict

class Inventory:
    def __init__(self):
        self.products = defaultdict(int)
    
    def add_product(self, product: Product, quantity: int):
        self.products[product] += quantity
        print(f"[Inventory]:{product} x {quantity} added to inventory. Total: {self.get_quantity(product)}")
        return
    
    def remove_product(self, product: Product, quantity: int):
        self.products[product] -= quantity
        print(f"[Inventory]:{product} x {quantity} @ ₹{product.price} removed from inventory. Total: {self.get_quantity(product)}")
        return

    def update_quantity(self): pass
    
    def get_quantity(self, product: Product) -> int:
        return self.products[product]
    
    def is_available(self, product: Product) -> bool:
        return self.products[product] > 0