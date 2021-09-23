# https://cses.fi/problemset/task/1141

def playlist(arr):
    dct = {}
    i = j = ans = 0
    while j<len(arr) and i<=j:
        if arr[j] in dct:
            new_i = dct[arr[j]] + 1
            while i < new_i:
                del dct[arr[i]]
                i += 1
        dct[arr[j]] = j
        ans = max(ans, j-i+1)
        j += 1

    print(ans)

n = int(input())
arr = [int(x) for x in input().split(' ')]
playlist(arr)
