from vending_machine_state import VendingMachineState
from product import Product 
from static import Coin, Note

class IdleState(VendingMachineState):
    def __init__(self, instance):
        self.vending_machine = instance
    
    def select_product(self, product: Product):
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.ready_state)
            print(f"Product selected: {product}")
        else:
            print(f"{product} is not available")
    
    def insert_coin(self, coin: Coin):
        print("[Error] please select a product first.")
    
    def insert_note(self, note: Note):
        print("[ERROR] Please select a product first")
        
    def dispense_product(self):
        print("[ERROR] Please select a product and make payment first")
    
    def return_change(self):
        print("[ERROR] No change to return")