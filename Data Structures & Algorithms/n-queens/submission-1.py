class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

    


   
        answers = []

        # Initialize empty board
        board = [["."] * n for _ in range(n)]

        # Helper function to check if placing a queen at (r,c) is safe
        def is_safe(r, c):
            # Check column
            for i in range(r):
                if board[i][c] == "Q":
                    return False
            # Check left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            # Check right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        # Backtracking function
        def backtrack(r):
            if r == n:
                # All queens placed; add current board to answers
                answers.append(["".join(row) for row in board])
                return

            for c in range(n):
                if is_safe(r, c):
                    board[r][c] = "Q"      # Place queen
                    backtrack(r + 1)       # Recurse to next row
                    board[r][c] = "."      # Remove queen (backtrack)

        # Start recursion from first row
        backtrack(0)
        return answers