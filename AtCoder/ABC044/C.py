from collections import defaultdict
def sol(n, a, arr):
    D = defaultdict(int)
    D[0] = 1
    for i in arr:
        for j, f in list(D.items()):
            D[i+j] = D[i+j]+f
    print(D[0]-1)

n, a = map(int, input().split())
arr = [int(x)-a for x in input().split()]
sol(n, a, arr)