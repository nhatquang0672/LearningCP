# https://cses.fi/problemset/task/1645

from collections import deque
def nearest_smaller_values(n, arr):
    dct = {}
    xx = deque()

    for i in range(n-1, -1, -1):
        while xx and xx[0][0] > arr[i]:
            val, idx = xx.popleft()
            dct[idx] = i
        xx.appendleft((arr[i], i))

    while xx:
        _, idx = xx.popleft()
        dct[idx] = -1

    for i in range(n):
        print(0 if dct[i] == -1 else dct[i]+1, end=' ')


n = int(input())
arr = [int(x) for x in input().split(' ')]
nearest_smaller_values(n, arr)