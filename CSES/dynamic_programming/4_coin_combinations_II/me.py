# https://cses.fi/problemset/task/1636

C = 10**9 + 7
def coin_combination_II(n, x, arr):
    mem = [0]*1000007
    mem[0] = 1
    for c in arr:
        for v in range(c, x+1):
            if v-c >= 0:
                mem[v] += mem[v-c]
                mem[v] = mem[v]% C
    print(mem[x])

n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
coin_combination_II(n, x, arr)