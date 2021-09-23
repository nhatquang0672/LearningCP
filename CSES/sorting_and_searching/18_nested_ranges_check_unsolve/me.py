# https://cses.fi/problemset/task/2168

def nested_ranges_check(n, mem, dct):
    for i in range(n):
        for j in range(i+1, n):
            l1, r1 = dct[i]
            l2, r2 = dct[j]
            if l1 == l2:
                if r1 == r2:
                    mem[i][j] = 1
                    mem[j][i] = 1
                elif r2 > r1:
                    mem[j][i] = 1
                else:
                    mem[i][j] = 1
            elif l1 < l2:
                if r1 >= r2:
                    mem[i][j] = 1
            else:
                if r2 >= r1:
                    mem[j][i] = 1
                    
    contain = []
    is_contained = []

    for i in range(n):
        is_true = 0
        for j in range(n):
            if mem[i][j] == 1:
                is_true = 1
                break
        contain.append(is_true)

    for i in range(n):
        is_true = 0
        for j in range(n):
            if mem[j][i] == 1:
                is_true = 1
                break
        is_contained.append(is_true)
    print(' '.join(str(x) for x in contain))
    print(' '.join(str(x) for x in is_contained))

n = int(input())
dct = {}
mem = [[0]*n for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split(' '))
    dct[i] = (a, b)

nested_ranges_check(n, mem, dct)
