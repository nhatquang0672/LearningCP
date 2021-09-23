
# https://cses.fi/problemset/task/2183

def missing_coin_sum(arr):
    arr = sorted(arr)
    curSum = 0
    for i in arr:
        if curSum+1 < i:
            print(curSum+1)
            return
        curSum += i
    print(curSum+1)

n = int(input())
arr = [int(x) for x in input().split(' ')]
missing_coin_sum(arr)