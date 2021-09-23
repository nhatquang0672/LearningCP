# https://cses.fi/problemset/task/1661

def subarray_sum_II(n, x, arr):
    s = ans = 0
    dct = {}
    for e in arr:
        dct[s] = dct[s]+1 if s in dct else 1
        s += e
        ans += dct.get(s-x, 0)
    print(dct)
    print(ans)

n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
subarray_sum_II(n, x, arr)