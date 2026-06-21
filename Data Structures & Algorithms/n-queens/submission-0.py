class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

    
        answers = []
        cols = set()
        posDiags = set()  # r + c
        negDiags = set()  # r - c
        board = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                # all queens placed
                answers.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r+c) in posDiags or (r-c) in negDiags:
                    continue  # cannot place queen

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                posDiags.add(r+c)
                negDiags.add(r-c)

                backtrack(r+1)

                # remove queen (backtrack)
                board[r][c] = "."
                cols.remove(c)
                posDiags.remove(r+c)
                negDiags.remove(r-c)

        backtrack(0)
        return answers