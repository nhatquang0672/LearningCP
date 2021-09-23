# https://cses.fi/problemset/task/1090/

def ferris_wheel(n, x, arr):
    i, j = 0, n-1
    ans = 0
    while i <= j:
        if arr[i] + arr[j] <= x:
            i += 1
        j -= 1
        ans += 1
    print(ans)

n, x = map(int, input().split())
arr = sorted([int(x) for x in input().split()])
ferris_wheel(n, x, arr)