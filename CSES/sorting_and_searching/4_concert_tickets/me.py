# https://cses.fi/problemset/task/1091

def bisect_right(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right)//2
        if arr[mid] > target:
            right = mid
        else:
            left = mid+1
    return left-1



def concert_tickets(n, m, hh, tt):
    sold_list = list(range(n+1))
    print(sold_list)
    for t in tt:
        rightmost = bisect_right(hh, t)
        if rightmost == -1:
            print(-1)
        else:
            print(hh[rightmost])
            del hh[rightmost]


n, m = map(int, input().split(' '))
hh = sorted([int(x) for x in input().split(' ')])
tt = [int(x) for x in input().split(' ')]
concert_tickets(n, m, hh, tt)

# arr = [1,3,4,7,7,22,55]
# ans = bisect_right(arr, 55)
# print(ans)