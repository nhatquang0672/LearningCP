
def permutations(ans, arr, start):
    if start >= len(arr):
        ans.append(arr[:])
    
    for i in range(start, len(arr)):
        arr[i], arr[start] = arr[start], arr[i]
        permutations(ans, arr, start+1)
        arr[i], arr[start] = arr[start], arr[i]

    return ans

ans = []
arr = [1,2,3,3]
permutations(ans, arr, 0)
print(ans)