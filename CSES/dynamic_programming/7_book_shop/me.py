# https://cses.fi/problemset/task/1158

def book_shop(n, x, h, s):
    bb = sorted(zip(h, s), key = lambda x: x[0])
    mem = [0]*(x+1)

    for i in range(n-1):
        fVal, fPage = bb[i]
        mem[fVal] = fPage
        for j in range(i+1, n):
            sVal, sPage = bb[j]
            if fVal + sVal > x: break
            mem[fVal+sVal] = max(mem[fVal+sVal], fPage + sPage)

        mem[coin] = page
        for i in range(coin+1, x+1):
            if i >= 2*coin: break
            mem[i] = max(mem[i-coin]+page, mem[i], mem[i-1])
    
    print(mem)


n, x = map(int, input().split())
h = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
book_shop(n, x, h , s)

# 4 100
# 4 8 5 3
# 5 12 8 1