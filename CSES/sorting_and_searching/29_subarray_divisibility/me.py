# https://cses.fi/problemset/task/1662

def subarray_divisibility(n, arr):
    ans, s = 0, 0
    dct = {}
    for e in arr:
        dct[s] = dct[s]+1 if s in dct else 1
        s = (s+e%n)%n
        ans += dct.get(s,0)

    print(ans)
            
n = int(input())
arr = [int(x) for x in input().split()]
subarray_divisibility(n, arr)