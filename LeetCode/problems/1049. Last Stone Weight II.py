# https://leetcode.com/problems/last-stone-weight-ii/

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        d = {0}
        s = sum(stones)
        for i in stones:
            d |= {a+i for a in d}
        return min(abs(2*i-s) for i in d)
        