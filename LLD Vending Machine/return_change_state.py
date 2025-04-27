from vending_machine_state import VendingMachineState
from product import Product
from static import Coin, Note

class ReturnChangeState(VendingMachineState):
    def __init__(self, instance):
        self.vending_machine = instance
    
    def select_product(self, product: Product):
        print("Please collect the change first")
    
    def insert_coin(self, coin: Coin):
        print("Please collect the change first")
        
    def insert_note(self, note: Note):
        print("Please collect the change first")
        
    def dispense_product(self):
        print("Product already dispensed. Please collect the change first")
    
    def return_change(self):
        change = self.vending_machine.total_payment
        
        if change > 0:
            print(f"Change returned: ₹{change:.2f}")
            self.vending_machine.reset_payment()
        else:
            print("No change to return")
        
        self.vending_machine.reset_selected_product()
        self.vending_machine.set_state(self.vending_machine.idle_state)