from threading import Thread, Lock
from snake_and_ladder_game import SnLGame

class GameMaster:
    _instance = None
    _lock = Lock()
    _game_count = 0
    
    def __init__(self):
        self.game_id = GameMaster._game_count
        self.games = []
        
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance
    
    def start_new_game(self, player_names):
        game = SnLGame(player_names)
        self.games.append(game)
        Thread(target=game.play).start()    # multithreading: each game is run on a different thread