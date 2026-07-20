class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            # outside grid means this side contributes 1 to perimeter
            if not (0 <= i < rows and 0 <= j < cols):
                return 1

            # water means this side contributes 1 to perimeter
            if grid[i][j] == 0:
                return 1

            # already visited land contributes 0
            if (i, j) in seen:
                return 0

            seen.add((i, j))

            return (
                dfs(i + 1, j) +
                dfs(i - 1, j) +
                dfs(i, j + 1) +
                dfs(i, j - 1)
            )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0