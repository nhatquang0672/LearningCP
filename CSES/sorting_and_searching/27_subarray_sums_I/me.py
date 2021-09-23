# https://cses.fi/problemset/task/1660

def subarray_sum_I_ver1(n, x, arr):
    ss = [0]*(n+1)
    ans = 0
    for i in range(n):
        ss[i] = ss[i-1]+arr[i]    
    print(ss)
    for i in range(n):
        for j in range(i, n):
            tpm_sum = ss[j]-ss[i-1]
            if tpm_sum == x:
                ans += 1
            if tpm_sum > x:
                break
    print(ans)

def subarray_sum_I(n, x, arr):
    dct = {}
    s = ans = 0
    for e in arr:
        dct[s] = dct[s]+1 if s in dct else 1
        s += e
        ans += dct.get(s-x, 0)
    print(ans)

n, x = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]
subarray_sum_I(n, x, arr)