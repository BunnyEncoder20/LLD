from board import Board
from dice import Dice 
from player import Player

class SnLGame:
    _game_count = 0

    def __init__(self, player_names):
        SnLGame._game_count += 1
        self._gameID = SnLGame._game_count
        self.board = Board()
        self.dice = Dice()
        self.players = [Player(name) for name in player_names]
        self.current_player_idx = 0
    
    def play(self):
        while not self._is_game_over():
            current_player = self.players[self.current_player_idx]
            dice_num = self.dice.roll()
            new_position = current_player.get_position() + dice_num
            
            if new_position <= self.board.get_board_size():
                current_player.set_position(self.board.get_new_position_after_snakes_or_ladder(new_position))
                print(f"[Game:{self._gameID}]: {current_player.get_name()} rolled a {dice_num} and moved to position {current_player.get_position()}")

            if current_player.get_position() == self.board.get_board_size():
                print(f"[Game:{self._gameID}]: 🥳 {current_player.get_name()} WINS !!! ")
                break
            
            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
    
    def _is_game_over(self):
        for player in self.players:
            if player.get_position() == self.board.get_board_size():
                return True
        return False