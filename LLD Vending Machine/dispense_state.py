from vending_machine_state import VendingMachineState
from product import Product
from static import Coin, Note

class DispenseState(VendingMachineState):
    def __init__(self, instance):
        self.vending_machine = instance
        
    def select_product(self, product: Product):
        print("[ERROR] Product already selected. Please collect the dispensed product")
        
    def insert_coin(self, coin: Coin):
        print("[ERROR] Payment already made. Please collect the dispensed product")
    
    def insert_note(self, note: Note):
        print("[ERROR] Payment already made. Please collect the dispensed product")
    
    def dispense_product(self):
        self.vending_machine.set_state(self.vending_machine.ready_state)
        product = self.vending_machine.selected_product
        self.vending_machine.total_payment -= product.price
        
        # print(f"[DEBUG]: total = {self.vending_machine.total_payment}")
        # print(f"[DEBUG]: product cost = {product.price}")
        # print(f"[DEBUG] Change to give back: {self.vending_machine.total_payment - product.price}")
        
        self.vending_machine.inventory.remove_product(product, 1)
        print(f"Product dispensed: {product}")
        self.vending_machine.set_state(self.vending_machine.return_change_state)
    
    def return_change(self):
        print("[ERROR] Please collect the dispensed product first.")