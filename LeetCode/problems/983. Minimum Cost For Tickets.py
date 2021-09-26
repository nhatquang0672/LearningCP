# https://leetcode.com/problems/minimum-cost-for-tickets/
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = sorted(days)
        s = set(days)
        dp = [0]*(days[-1]+1)
        for i in range(1, days[-1]+1):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(costs[0]+dp[i-1], costs[1] +dp[i-7] if i-7>=0 else costs[1], costs[2]+dp[i-30] if i-30>=0 else costs[2])
        # print(dp)
        return dp[-1]