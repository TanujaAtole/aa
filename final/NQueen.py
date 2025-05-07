import time

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  # To store the position of queens
        self.columns = [False] * n  # To track columns that are occupied by queens
        self.diag1 = [False] * (2 * n - 1)  # Diagonal from top-left to bottom-right
        self.diag2 = [False] * (2 * n - 1)  # Diagonal from top-right to bottom-left

    def print_board(self):
        """Print the chessboard with queens marked as 'Q' and empty spots as '.'"""
        print("Solution:")
        for row in range(self.n):
            board_row = ['Q' if col == self.board[row] else '.' for col in range(self.n)]
            print(' '.join(board_row))
        print()

    def is_safe(self, row, col):
        """Check if placing a queen at (row, col) is safe"""
        return not (self.columns[col] or self.diag1[row - col + self.n - 1] or self.diag2[row + col])

    def solve_backtracking(self, row=0):
        """Solve the N-Queens problem using Backtracking"""
        if row == self.n:
            self.print_board()
            return True
        for col in range(self.n):
            if self.is_safe_backtracking(row, col):
                self.board[row] = col
                if self.solve_backtracking(row + 1):
                    return True
                self.board[row] = -1  # Backtrack
        return False

    def is_safe_backtracking(self, row, col):
        """Check if placing a queen at (row, col) is safe for backtracking"""
        for prev_row in range(row):
            if (self.board[prev_row] == col or
                self.board[prev_row] - prev_row == col - row or
                self.board[prev_row] + prev_row == col + row):
                return False
        return True

    def branch_and_bound(self):
        """Solve the N-Queens problem using Branch and Bound"""
        start_time = time.time()
        if self.solve_with_bound(0):
            print("Solution found using Branch and Bound!")
        else:
            print("No solution exists.")
        print(f"Time taken: {time.time() - start_time:.5f} seconds")

    def solve_with_bound(self, row):
        """Solve the N-Queens problem using Branch and Bound"""
        if row == self.n:
            self.print_board()
            return True
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.columns[col] = True
                self.diag1[row - col + self.n - 1] = True
                self.diag2[row + col] = True

                if self.solve_with_bound(row + 1):
                    return True

                # Backtrack
                self.board[row] = -1
                self.columns[col] = False
                self.diag1[row - col + self.n - 1] = False
                self.diag2[row + col] = False
        return False

def n_queens_solver(n):
    """Solving the N-Queens problem using both Backtracking and Branch and Bound"""
    print(f"Solving the {n}-Queens problem using Backtracking...\n")
    n_queens = NQueens(n)
    n_queens.solve_backtracking()

    print(f"\nSolving the {n}-Queens problem using Branch and Bound...\n")
    n_queens = NQueens(n)
    n_queens.branch_and_bound()

if __name__ == "__main__":
    n = int(input("Enter the value of N for N-Queens problem: "))
    n_queens_solver(n)
