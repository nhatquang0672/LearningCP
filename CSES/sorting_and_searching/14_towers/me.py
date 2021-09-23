# https://cses.fi/problemset/task/1073

def towers(n, arr):
    tt = []
    for i in range(n):
        print(tt)
        lo, hi = 0, len(tt)
        while lo < hi:
            mid = (lo+hi) // 2
            if arr[i] < tt[mid]:
                hi = mid
            else:
                lo = mid+1
        if lo == len(tt):
            tt.append(arr[i])
        else:
            tt[lo] = arr[i]
    print(len(tt))
n = int(input())
arr = [int(x) for x in input().split(' ')]
towers(n, arr)