class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player 
            if self.check_winner():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                return True
            elif " " not in self.board:
                self.display_board()
                print("It's a draw!")
                return True
            self.switch_player()
            return False
        else:
            print("This position is already taken!")
            return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

def main():
    game = TicTacToe()
    game_over = False
    while not game_over:
        game.display_board()
        position = int(input(f"Player {game.current_player}, enter your move (0-8): "))
        if 0 <= position <= 8:
            game_over = game.make_move(position)
        else:
            print("Invalid position. Please enter a number between 0 and 8.")

if __name__ == "__main__":
    main()

