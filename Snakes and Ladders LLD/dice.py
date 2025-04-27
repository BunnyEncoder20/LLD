from random import randint

class Dice:
    MIN_VALUE = 1
    MAX_VALUE = 6
    
    def roll(self):
        return randint(Dice.MIN_VALUE, Dice.MAX_VALUE)