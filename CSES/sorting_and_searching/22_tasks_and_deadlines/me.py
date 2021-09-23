# https://cses.fi/problemset/task/1630/

def tasks_and_deadlines(n, arr):
    reward = 0
    start = 0
    for e in arr:
        end = start + e[0]
        reward += e[1] - end
        start = end
    print(reward)

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    arr.append((a, b))

arr = sorted(arr, key = lambda k: k[0])
tasks_and_deadlines(n, arr)