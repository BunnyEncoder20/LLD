from player import Player

from colorama import init, Fore, Back
init(autoreset=True)

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.moves_count = 0
        self.winner = None
        
        # calc for winner
        self.rowsum = [0]*3
        self.colsum = [0]*3
        self.diagsum = 0
        self.antidiag = 0
    
    def make_move(self, row, col, current_player: Player):
        if self.grid[row][col] != " ": raise ValueError("❌ Position already marked")
        
        # normally
        self.grid[row][col] = "O" if current_player.get_symbol() == "O" else "X"
        self.moves_count += 1
        
        # update board metrics
        score = 1 if current_player.get_symbol() == "X" else -1
        self.rowsum[row] += score
        self.colsum[col] += score
        if row == col: self.diagsum += score
        if row+col == 2: self.antidiag += score
        
        # check if won
        if (
            abs(self.rowsum[row]) == 3 or
            abs(self.colsum[col]) == 3 or
            abs(self.diagsum) == 3 or
            abs(self.antidiag) == 3
        ): 
            self.winner = current_player
    
    def is_full(self):
        return self.moves_count == 9

    def get_winner(self):
        return self.winner
    
    def print_board(self):
        for row in range(3):
            print(Fore.WHITE + " | ".join(self.grid[row]))
            if row != 2: print(Fore.WHITE + "----------")
        print()
