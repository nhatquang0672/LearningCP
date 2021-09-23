# https://cses.fi/problemset/task/1633

C = 10**9+7

def dice_combination(n):
    mem = [0]*(n+1)
    mem[0] = 1
    for i in range(1, n+1):
        for j in range(1, 7):
            mem[i] += mem[i-j] if i-j >=0 else 0
        mem[i] = mem[i]%C
    print(mem[-1])
n = int(input())
dice_combination(n)