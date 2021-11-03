def C(n, r):
    if r < 0 or n < r: return 0
    return fact[n] * ifac[r] * ifac[n-r] % MOD

MOD = 10**9 + 7
H, W, A, B = map(int, input().split())
n = H + W
fact = [1] * n
ifac = [1] * n
inv = [1] * n
for x in range(2, n):
    inv[x] = inv[MOD % x] * (MOD - MOD // x) % MOD
    fact[x] = fact[x-1] * x % MOD
    ifac[x] = ifac[x-1] * inv[x] % MOD
ans = 0
for j in range(B, W):
    ans = (ans + C(H-1-A+j, j) * C(W-j+A-2, A-1)) % MOD
print(inv)
print(fact)
print(ifac)
print(ans)
