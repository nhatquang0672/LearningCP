# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dq = collections.deque([(0,0,0,0)])
        visited = set()
        while dq:
            x, y, obstacles, d = dq.popleft()
            for r, c in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == 1 and obstacles < k and (r, c, obstacles+1) not in visited:
                        visited.add((r, c, obstacles+1))
                        dq.append((r, c, obstacles+1, d+1))
                    if grid[r][c] == 0 and (r, c, obstacles) not in visited:
                        if (r, c) == (m-1, n-1): return d+1
                        visited.add((r, c, obstacles))
                        dq.append((r, c, obstacles, d+1))
        return -1


x = Solution()
a, b = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]], 1
print(x.shortestPath(a, b))
