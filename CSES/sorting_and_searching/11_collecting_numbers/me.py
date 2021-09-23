# https://cses.fi/problemset/task/2216

def collecting_numbers(n, arr):
    xx = [0]*(n+1)
    for i in range(n):
        xx[arr[i]] = i

    ans, last = 1, 0
    for i in range(1, n+1):
        if last > xx[i]:
            ans += 1
        last = xx[i]
    print(ans)

n = int(input())
arr = [int(x) for x in input().split(' ')]

collecting_numbers(n, arr)

# 8
# 1 4 2 6 5 3