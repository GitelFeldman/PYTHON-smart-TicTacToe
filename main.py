from player import Player
from game import Game

from player import Player
from computer_player import Computer_Player
from humen_player import Human_Player
print("Choose the game type:")
print("1. Human vs Human")
print("2. Human vs Computer")
choice = input("Enter the number of your choice: ")
if choice == "1":
    player1 = Human_Player("gitty", 'x')
    player2 = Human_Player("itty", 'o')
elif choice == "2":
    player1 = Human_Player("gitty", 'x')
    player2 = Computer_Player("computer", 'o')  # computer player
else:
    print("Invalid choice. Defaulting to Human vs Human.")

game1 = Game(player1, player2)
game1.Play()

