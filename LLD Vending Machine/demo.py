from vending_machine import VendingMachine
from product import Product
from static import Coin,Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine.get_instance()

        # Add products to the inventory
        coke = Product("Coke", 25)
        pepsi = Product("Pepsi", 20)
        water = Product("Water", 10)

        vending_machine.inventory.add_product(coke, 5)
        vending_machine.inventory.add_product(pepsi, 3)
        vending_machine.inventory.add_product(water, 2)

        # Select a product
        vending_machine.select_product(coke)

        # Insert coins
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.FIVE)

        # Insert a note
        vending_machine.insert_note(Note.FIVE)

        # Dispense the product
        vending_machine.dispense()

        # Return change
        vending_machine.return_change()

        # Select another product
        vending_machine.select_product(pepsi)

        # Insert insufficient payment
        vending_machine.insert_coin(Coin.TEN)

        # Try to dispense the product
        vending_machine.dispense()

        # Insert more money
        vending_machine.insert_note(Note.FIVTY)

        # Dispense the product
        vending_machine.dispense()

        # Return change
        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()