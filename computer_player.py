from player import Player
import time

class Computer_Player(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)
        self.cnt_runs = 0  # Variable to count the number of times the algorithm runs
        self.exec_time_avg = 0  # Average execution time of the algorithm
        self.memo = {}  # Dictionary to store already computed states
    
    def get_runtime_avg(self):
        print(f"Average execution time: {self.exec_time_avg} ms")


#================= minimax with the best improvements - alpha beta pruning and memoization===============
#=================only 1.77 milliseconds=================
    def minimax(self, board, depth, is_maximizing_player, alpha, beta):
        board_state = ''.join(board.board)  # Convert the board to a string to store in memory

        # If the result for this state is already computed, return it from memory
        if board_state in self.memo:
            return self.memo[board_state]

        # Terminal state (win or draw)
        if board.is_winner(self.marker):
            return 1
        elif board.is_winner('x' if self.marker == 'o' else 'o'):
            return -1
        elif board.is_drow():
            return 0

        if is_maximizing_player:
            best = -float('inf')
            for i in range(9):
                if board.board[i] == ' ':
                    board.board[i] = self.marker
                    score = self.minimax(board, depth + 1, False, alpha, beta)
                    board.board[i] = ' '  # Backtrack
                    best = max(best, score)
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break  # Beta cutoff
        else:
            best = float('inf')
            for i in range(9):
                if board.board[i] == ' ':
                    board.board[i] = 'x' if self.marker == 'o' else 'o'
                    score = self.minimax(board, depth + 1, True, alpha, beta)
                    board.board[i] = ' '  # Backtrack
                    best = min(best, score)
                    beta = min(beta, best)
                    if beta <= alpha:
                        break  # Alpha cutoff

        # Store the result in memory
        self.memo[board_state] = best
        return best


    def _computer_move(self, board):
        # Start measuring execution time
        start_time = time.time()

        best_score = -float('inf')
        best_move = None
        alpha = -float('inf')
        beta = float('inf')

        # Search for the best move using the minimax algorithm
        for i in range(9):
            if board.board[i] == ' ':
                board.board[i] = self.marker  # Test the computer's move
                score = self.minimax(board, 0, False, alpha, beta)
                board.board[i] = ' '  # Backtrack
                if score > best_score:
                    best_score = score
                    best_move = i

        # Execute the best move found
        board.make_move(best_move, self)

        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000

        # Update the average execution time
        self.cnt_runs += 1
        self.exec_time_avg = ((self.exec_time_avg * (self.cnt_runs - 1)) + execution_time_ms) / self.cnt_runs

        return board  # Return the updated board



# ===================def minimax with alpha beta pruning=======================
#====================3.2 milliseconds=======================
    # def minimax(self, board, depth, is_maximizing_player, alpha, beta):
    #     # Terminal state (win or draw)
    #     if board.is_winner(self.marker):
    #         return 1
    #     elif board.is_winner('x' if self.marker == 'o' else 'o'):
    #         return -1
    #     elif board.is_drow():
    #         return 0

    #     if is_maximizing_player:
    #         best = -float('inf')
    #         for i in range(9):
    #             if board.board[i] == ' ':
    #                 board.board[i] = self.marker
    #                 score = self.minimax(board, depth + 1, False, alpha, beta)
    #                 board.board[i] = ' '
    #                 best = max(best, score)
    #                 # Update alpha
    #                 alpha = max(alpha, best)
    #                 # Cutoff if beta is less than or equal to alpha
    #                 if beta <= alpha:
    #                     break
    #         return best
    #     else:
    #         best = float('inf')
    #         for i in range(9):
    #             if board.board[i] == ' ':
    #                 board.board[i] = 'x' if self.marker == 'o' else 'o'
    #                 score = self.minimax(board, depth + 1, True, alpha, beta)
    #                 board.board[i] = ' '
    #                 best = min(best, score)
    #                 # Update beta
    #                 beta = min(beta, best)
    #                 # Cutoff if alpha is greater than or equal to beta
    #                 if beta <= alpha:
    #                     break
    #         return best


    # def _computer_move(self, board):
    #      # Start measuring execution time
    #     start_time = time.time()

    #     best_score = -float('inf')
    #     best_move = None
    #     alpha = -float('inf')  # Start with a very low alpha
    #     beta = float('inf')    # Start with a very high beta

    #     # Search for the best move using the minimax algorithm
    #     for i in range(9):
    #         if board.board[i] == ' ':
    #             board.board[i] = self.marker  # Test the computer's move
    #             score = self.minimax(board, 0, False, alpha, beta)
    #             board.board[i] = ' '  # Backtrack
    #             if score > best_score:
    #                 best_score = score
    #                 best_move = i

    #     # Execute the best move found
    #     board.make_move(best_move, self)

        
    #     end_time = time.time()
    #     execution_time_ms = (end_time - start_time) * 1000

    #     # Update the average execution time
    #     self.cnt_runs += 1
    #     self.exec_time_avg = ((self.exec_time_avg * (self.cnt_runs - 1)) + execution_time_ms) / self.cnt_runs

    #     return board  # Return the updated board
    



#============================ minimax without improvements =========================
#============================ 27.98 milliseconds========================
    # def minimax(self, board, depth, is_maximizing_player):
    #     # Terminal state (win or draw)
    #     if board.is_winner(self.marker):
    #         return 1
    #     elif board.is_winner('x' if self.marker == 'o' else 'o'):
    #         return -1
    #     elif board.is_drow():
    #         return 0

    #     if is_maximizing_player:
    #         best = -float('inf')
    #         for i in range(9):
    #             if board.board[i] == ' ':
    #                 board.board[i] = self.marker
    #                 score = self.minimax(board, depth + 1, False)
    #                 board.board[i] = ' '
    #                 best = max(best, score)
    #         return best
    #     else:
    #         best = float('inf')
    #         for i in range(9):
    #             if board.board[i] == ' ':
    #                 board.board[i] = 'x' if self.marker == 'o' else 'o'
    #                 score = self.minimax(board, depth + 1, True)
    #                 board.board[i] = ' '
    #                 best = min(best, score)
    #         return best

    # def _computer_move(self, board):

    #     # Start measuring execution time
    #     start_time = time.time()

    #     best_score = -float('inf')
    #     best_move = None

    #     # Search for the best move using the minimax algorithm
    #     for i in range(9):
    #         if board.board[i] == ' ':
    #             board.board[i] = self.marker  # Test the computer's move
    #             score = self.minimax(board, 0, False)
    #             board.board[i] = ' '  # Backtrack
    #             if score > best_score:
    #                 best_score = score
    #                 best_move = i

    #     # Execute the best move found
    #     board.make_move(best_move, self)


    #     end_time = time.time()
    #     execution_time_ms = (end_time - start_time) * 1000

    #     # Update the average execution time
    #     self.cnt_runs += 1
    #     self.exec_time_avg = ((self.exec_time_avg * (self.cnt_runs - 1)) + execution_time_ms) / self.cnt_runs

    #     return board  # Return the updated board