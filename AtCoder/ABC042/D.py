m, n, a, b = map(int, input().split())
dp = [[0]*n for _ in range(m)]
invalid = set()
C = 10**9+7
for i in range(m-a, m):
    for j in range(0, b):
        invalid.add((i, j))
dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if (i, j) in invalid: continue
        if i >= 1: dp[i][j] += dp[i-1][j]
        if j >= 1: dp[i][j] += dp[i][j-1]
        dp[i][j] = dp[i][j] % C
print(dp[-1][-1])