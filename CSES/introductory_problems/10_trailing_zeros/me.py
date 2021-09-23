# https://cses.fi/problemset/task/1618


num = int(input())
ans = 0
i = 1
while num // 5**i >= 1:
    ans += num // 5**i
    i += 1
print(ans)