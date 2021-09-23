# https://cses.fi/problemset/task/1619

def restaurant_customers(dct):
    arr = sorted(dct, key=lambda a: a[0])
    ans, cur = 0, 0
    for e in arr:
        cur += e[1]
        ans = max(ans, cur)
    print(ans)

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    arr.append((a, 1))
    arr.append((b, -1))

restaurant_customers(arr)