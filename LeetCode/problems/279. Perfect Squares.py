# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        ppss = []
        for i in range(1, n+1):
            if i**0.5 == int(i**0.5): ppss.append(i)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = min([dp[i-j] for j in ppss if i-j>=0])+1
        
        return dp[-1]