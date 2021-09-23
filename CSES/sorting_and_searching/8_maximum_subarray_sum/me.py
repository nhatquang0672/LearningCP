# https://cses.fi/problemset/task/1643

def maximum_subarray_sum(arr):
    maxSum, curSum = float('-inf'), 0
    for e in arr:
        if curSum + e <= e:
            curSum = e
        else:
            curSum += e
        maxSum = max(maxSum, curSum)
    
    print(maxSum)

n = int(input())
arr = [int(x) for x in input().split(' ')]
maximum_subarray_sum(arr)