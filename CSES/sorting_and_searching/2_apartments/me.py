

def apartments(n, m, k, arr, brr):
    ans = 0
    a, b = 0, 0
    while a < n and b < m:
        if brr[b] - k <= arr[a] and arr[a] <= brr[b]+k:
            a += 1
            b += 1
            ans += 1
        elif arr[a] < brr[b] - k :
            a += 1
        else:
            b += 1

    print(ans)


n, m, k = [int(x) for x in input().split(' ')]
Arr = sorted([int(x) for x in input().split(' ')])
Brr = sorted([int(x) for x in input().split(' ')])
apartments(n, m, k, Arr, Brr)