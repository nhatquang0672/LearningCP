# https://cses.fi/problemset/task/1164

from sys import stdin, stdout
 
readln = stdin.readline
writelst = lambda x: stdout.write(' '.join(map(str, x)))
writenum = lambda x: stdout.write(str(x) + '\n')
writestr = lambda x: stdout.write(x)

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
    writenum(maxroom)
    writelst(occupied[1:])


n = int(readln())
arr = []
for i in range(1, n+1):
    l, r = map(int, readln().split())
    arr.append((l, i))
    arr.append((r+1, -i))

arr.sort()
room_allocation(n, arr)