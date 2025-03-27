class Board():
    def __init__(self):
        self.board = [' '] * 9


#print the board
    def __str__(self):
        result = ""
        for i in range(0, 9):
            result += self.board[i] + " | "
            if (i + 1) % 3 == 0:
                result += '\n'
        return result

#poot the marker in the board and check if the place is not already taken
    def make_move(self, place, player):
        if self.board[place] != ' ':
            raise IndexError("place is already taken")
        else:
            self.board[place] = player.marker

#check if the player is the winner
    def is_winner(self, marker):
        if (self.board[0] == self.board[1] == self.board[2] == marker or
                self.board[3] == self.board[4] == self.board[5] == marker or
                self.board[6] == self.board[7] == self.board[8] == marker):
            return True
        if (self.board[0] == self.board[4] == self.board[8] == marker or
                self.board[2] == self.board[4] == self.board[6] == marker):
            return True
        if (self.board[0] == self.board[3] == self.board[6] == marker or
                self.board[1] == self.board[4] == self.board[7] == marker or
                self.board[2] == self.board[5] == self.board[8] == marker):
            return True
        return False
#check if the board is full
    def is_drow(self):
        for i in self.board:
            if i == ' ':
                return False
        return True

