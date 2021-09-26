# https://leetcode.com/problems/2-keys-keyboard/
class Solution:
    def minSteps(self, n: int) -> int:
        if n <= 1: return 0
        dp = [math.inf]*(n+1)
        dp[0] = dp[1] = 0
        for i in range(2, n+1):
            if dp[i] == math.inf: dp[i] = i
            for j in range(i*2, n+1, i):
                dp[j] = min(dp[j], dp[j-i]+2 if j == i*2 else dp[i]+(j-i)//i+1)
        return dp[-1]