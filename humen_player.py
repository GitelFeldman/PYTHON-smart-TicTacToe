from player import Player
from board import Board

class Human_Player(Player):
    def __init__(self, marker, board):
        super().__init__(marker, board)

    def _player_move(self, board):
        move_made = False
        while not move_made:
            try:
                move = int(input(f"Player {self.marker}, enter your move (0-8): "))
                board.make_move( move,self)
                move_made = True
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
            except Exception as e:
                print(e)