from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Put all initially rotten oranges in the queue
        # Count fresh oranges
        seen=set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c,0))

                elif grid[r][c] == 1:
                    fresh += 1
        ans=0  
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,am=q.popleft()
            if (r,c) not in seen and grid[r][c]==1:
                seen.add((r,c))
                ans=max(ans,am)
                fresh-=1
            for f1,f2 in directions:
                rc=r+f1
                cc=c+f2
                if 0<=rc<ROWS and 0<=cc<COLS and (rc,cc) not in seen and grid[rc][cc]==1:
                    q.append((rc,cc,am+1))
        if fresh>0: 
            return -1
        return ans


                



#         minutes = 0
#         directions = [(1,0), (-1,0), (0,1), (0,-1)]

#         # Each while-loop round is one minute
#         while q and fresh > 0:
#             for _ in range(len(q)):
#                 r, c = q.popleft()

#                 for dr, dc in directions:
#                     nr, nc = r + dr, c + dc

#                     if (
#                         0 <= nr < ROWS and
#                         0 <= nc < COLS and
#                         grid[nr][nc] == 1
#                     ):
#                         grid[nr][nc] = 2
#                         fresh -= 1
#                         q.append((nr, nc))

#             minutes += 1

#         if fresh > 0:
#             return -1

#         return minutes
