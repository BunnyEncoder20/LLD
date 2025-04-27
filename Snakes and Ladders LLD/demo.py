from game_manager import GameMaster

class SnakeAndLadderDemo:
    def run():
        game_master = GameMaster.get_instance()
        
        # Start Game 1
        players_group1 = ["Player 1", "Player 2", "Player 3"]
        game_master.start_new_game(players_group1)
        
        players_group2 = ["Player 4", "Player 5"]
        game_master.start_new_game(players_group2)

if __name__ == "__main__":
    SnakeAndLadderDemo.run()