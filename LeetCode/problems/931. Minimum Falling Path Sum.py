# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += min([matrix[x][y] for x, y in[(i-1, j-1), (i-1, j), (i-1, j+1)] if 0 <= x < m and 0 <= y < n])
        return min(matrix[-1])