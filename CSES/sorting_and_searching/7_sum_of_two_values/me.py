# https://cses.fi/problemset/task/1640

def two_sum(arr, target):
    dct = {}
    for i in range(len(arr)):
        if target-arr[i] not in dct:
            dct[arr[i]] = i
        else:
            print("%d %d" % (i+1, dct[target-arr[i]]+1))
            return
    print('IMPOSSIBLE')

n, x = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ') ]
two_sum(arr, x)