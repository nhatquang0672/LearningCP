# https://cses.fi/problemset/task/1637
def removing_digits(n):
    mem = [float('inf')] * (n+1)
    mem[0] = 0
    for i in range(1, n+1):
        tmp = i
        while tmp:
            mem[i] = min(mem[i], mem[i-tmp%10]+1)
            tmp //= 10
    print(mem[-1])

n = int(input())
removing_digits(n)



