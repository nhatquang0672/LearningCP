# https://cses.fi/problemset/task/1634

def minimizing_coins(n, x, arr):
    mem = [float('inf')]*(x+1)
    mem[0] = 0
    arr = sorted(arr)

    for i in range(1, x+1):
        for c in arr:
            if i-c < 0: break
            mem[i] = min(mem[i], mem[i-c]+1)
            
    print(mem[-1] if mem[-1] != float('inf') else -1) 

n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
minimizing_coins(n, x, arr)

# 3 11
# 2 5 7