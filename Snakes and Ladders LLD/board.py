from snake import Snake
from ladder import Ladder

class Board:
    BOARD_SIZE = 100
    
    def __init__(self):
        self.snakes = []
        self.ladders = []
        self._initialize_snakes_n_ladders()
    
    def _initialize_snakes_n_ladders(self):
        # initialize snakes
        self.snakes.append(Snake(16,6))
        self.snakes.append(Snake(48,26))
        self.snakes.append(Snake(64,50))
        self.snakes.append(Snake(83,75))
        self.snakes.append(Snake(99,9))
        
        # initialize ladders
        self.ladders.append(Ladder(1, 38))
        self.ladders.append(Ladder(4, 14))
        self.ladders.append(Ladder(9, 31))
        self.ladders.append(Ladder(21, 42))
        self.ladders.append(Ladder(28, 84))
        
    def get_board_size(self):
        return Board.BOARD_SIZE
    
    def get_new_position_after_snakes_or_ladder(self, position):
        for snake in self.snakes:
            if snake.get_head() == position:
                return snake.get_tail()
        
        for ladder in self.ladders:
            if ladder.get_bottom() == position:
                return ladder.get_top()
        
        # nothing in this position
        return position