# https://cses.fi/problemset/task/1074

n = int(input())
arr = sorted([int(x) for x in input().split(' ')])
p = arr[n//2]
ans = 0
for i in arr:
    ans += abs(i-p)

print(ans)