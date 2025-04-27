from game import GameMaster
from player import Player

class TicTacToe_Demo:
    @staticmethod
    def run():
        # init players
        player1 = Player("Player1", 'X')
        player2 = Player("Player2", 'O')
        
        # init game
        game = GameMaster(player1, player2)
        game.play()

if __name__ == '__main__':
    TicTacToe_Demo.run()