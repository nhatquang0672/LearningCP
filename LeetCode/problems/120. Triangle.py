# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row, p in enumerate(triangle):
            max_prev_col = len(p)-1
            for col, val in enumerate(p):
                triangle[row][col] += min([triangle[x][y] for x, y in[(row-1, col), (row-1, col-1)] if 0<=x and 0<=y<max_prev_col], default = 0)
        return min(triangle[-1])