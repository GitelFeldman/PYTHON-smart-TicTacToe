from board import Board
from player import Player
import copy

from computer_player import Computer_Player  # Import the Computer_Player class
from board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.turn = player1

    def _board_full(self):
        # Check if the board is full (no empty spaces left)
        return not ' ' in self.board.board

    def _check_win(self, letter):
        # Check if the given marker (letter) has a winning combination
        win_combs = [letter, letter, letter]
        b = self.board.board
        return b[:3] == win_combs or b[3:6] == win_combs or b[6:] == win_combs or \
               b[:7:3] == win_combs or b[1:8:3] == win_combs or b[2::3] == win_combs or \
               b[::4] == win_combs or b[2:7:2] == win_combs

    def Play(self):
        # Main game loop
        print("Welcome to Tic Tac Toe!")
        print("player 1  " + self.player1.name)
        print("player 2  " + self.player2.name)

        for i in range(0, 9):
            print(self.board.__str__())  # Print the board at every step
            if self.turn.name == "computer":
                self.turn._computer_move(self.board)  # Let the computer make a move
            else:
                self.turn._player_move(self.board)  # Let the human player make a move

            if self.board.is_winner(self.turn.marker):
                # Check if the current player is the winner
                print(self.board.__str__())
                print(self.turn.name + " is the winner!!")
                if self.turn.name == "computer":
                    self.player2.get_runtime_avg()  # Print the computer's average runtime
                break
            elif self.turn == self.player1:
                # Switch turn to player 2
                self.turn = self.player2
            else:
                # Switch turn to player 1
                self.turn = self.player1
