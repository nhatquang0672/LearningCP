# https://cses.fi/problemset/task/1641

def sum_of_two_values(arr, x, left, right):
    if right-left+1 < 2:
        return (-1, -1)
    i, j = left, right
    while i < j:
        if arr[i][0]+arr[j][0] == x:
            return (arr[i][1], arr[j][1])
        elif arr[i][0]+arr[j][0] > x:
            j -= 1
        else:
            i += 1
    return (-1, -1)

def sum_of_three_values(arr, x, left, right):
    if right-left+1 < 3:
        print('IMPOSSIBLE')
    for i in range(left, right+1):
        s2 = sum_of_two_values(arr, x-arr[i][0], i+1, right)
        if s2[0] != -1:
            print("%d %d %d" % (arr[i][1]+1, s2[0]+1, s2[1]+1))
            return
    print('IMPOSSIBLE')



n, x = map(int, input().split(' '))
arr = [int(x) for x in input().split(' ')]
aa = []
for i in range(n):
    aa.append((arr[i], i))

aa = sorted(aa, key = lambda k: k[0])
sum_of_three_values(aa, x, 0, n-1)