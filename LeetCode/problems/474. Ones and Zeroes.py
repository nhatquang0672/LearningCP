# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(s):
            z, o = 0, 0
            for c in s:
                if c == '0': z += 1
                else: o += 1
            return (z, o)
        arr = [count(x) for x in strs]
        ans = 0
        dp = {(0, 0, 0)}
        for a, b in arr:
            dp |= {(a+x, b+y, z+1) for x, y, z in dp if a+x<=m and b+y<=n}
        return max([z for x, y, z in dp if x<=m and y<=n], default = 0)