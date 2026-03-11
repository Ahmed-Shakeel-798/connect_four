class ConnectFour:
    ROWS = 6
    COLS = 7
    COL_LABELS = "ABCDEFG"

    def __init__(self):
        self.board = [["." for _ in range(self.COLS)] for _ in range(self.ROWS)] 
        self.current_player = "X"

    def legal_moves(self):
        """Return list of column indices where a move is possible."""
        return [c for c in range(self.COLS) if self.board[0][c] == "."] # A column is full if the top row is filled.

    def move(self, col):
        """Drop a piece in the specified column index (0–6)."""
        if col not in range(self.COLS):
            raise ValueError("Column out of range")

        if col not in self.legal_moves():
            raise ValueError("Column is full")

        for row in reversed(range(self.ROWS)):
            if self.board[row][col] == ".":
                self.board[row][col] = self.current_player
                self.current_player = "O" if self.current_player == "X" else "X"
                return

    def print_board(self):
        """Print the board to terminal."""
        print(" " + " ".join(self.COL_LABELS))
        for row in self.board:
            print("|" + " ".join(row) + "|")
        print("+" + "--" * self.COLS + "+")


# Example usage
board = ConnectFour()

board.print_board()
board.move(2)   # drop in column C
board.move(2)
board.move(3)

board.print_board()

print("Legal moves:", [ConnectFour.COL_LABELS[c] for c in board.legal_moves()])