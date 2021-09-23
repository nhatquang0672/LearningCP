# https://cses.fi/problemset/task/1164
import heapq

def room_allocation(n, pp):
    frees = []
    occupied = [-1]*(n+1)
    maxroom = 0
    for ele in pp:
        i = ele[1]
        if i > 0:
            if frees:
                occupied[i] = frees.pop()
            else:
                maxroom += 1
                occupied[i] = maxroom
        else:
            frees.append(occupied[-i])
    print(maxroom)
    for i in range(1, n+1):
        print(occupied[i], end=' ')    

n = int(input())
arr = []
for i in range(1, n+1):
    l, r = map(int, input().split(' '))
    arr.append((l, i))
    arr.append((r+1, -i))

arr = sorted(arr)
room_allocation(n, arr)