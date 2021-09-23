# https://cses.fi/problemset/task/1629

def movie_festival(arr):
    arr = sorted(arr, key = lambda a: a[1])
    ans = 1
    last = arr[0]

    for i in range(1, len(arr)):
        cur = arr[i]
        if cur[0] >= last[1]:
            ans += 1
            last = cur
    print(ans)


n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    arr.append((a, b))

movie_festival(arr)