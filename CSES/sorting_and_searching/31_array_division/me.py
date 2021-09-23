# https://cses.fi/problemset/task/1085

def count(target, arr):
    count = 1
    cur = arr[0]
    for i in range(1, len(arr)):
        cur += arr[i]
        if cur > target:
            count += 1
            cur = arr[i]
    return count

def array_division(n, k, arr):
    left = max(arr)
    right = n*left
    while left<right:
        mid = (left+right)//2
        if count(mid, arr) > k:
            left = mid + 1
        else:
            right = mid
    print(left)
    
n, k = map(int, input().split())
xx = [int(x) for x in input().split()]
array_division(n, k, xx)
