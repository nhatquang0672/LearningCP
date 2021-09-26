# https://leetcode.com/contest/weekly-contest-260/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s0 = sum(grid[0])
        ans = math.inf
        sr0, sr1 = 0, 0
        for i in range(n):
            sr0 += grid[0][i]
            sr1 += grid[1][i]
            ans = min(ans, max(s0-sr0, sr1-grid[1][i]))
        return ans