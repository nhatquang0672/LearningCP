
def subarray_distinct_values_old(n, x, arr):
    se = set()
    ans = 0
    i, j = 0, 0
    while i < n:
        # print(i, j, ans, se)
        if j >= n:
            j -= 1
            ans += (j-i+1)*(j-i+2) // 2
            break        

        se.add(arr[j])
        if len(se) <= x:
            j += 1
        else:
            j -= 1
            ans += j-i+1
            se.clear()
            i += 1
            j = i
        # print(i, j, ans, se)
        # print('-------------------------')
    print(ans)

def subarray_distinct_values(n, x, arr):
    dct = {}
    ans = 0
    i, j = 0, 0
    while j < n:

        dct[arr[j]] = dct[arr[j]] + 1 if arr[j] in dct else 1     
        while len(dct) > x:
            if dct[arr[i]] - 1 == 0:
                del dct[arr[i]]
            else:
                dct[arr[i]] -= 1
            i += 1
        ans += j-i+1
        j += 1
    print(ans)    


n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
subarray_distinct_values(n, x, arr)