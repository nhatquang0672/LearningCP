# https://cses.fi/problemset/task/1622

def create_strings(arr):
    def perm(ans, start, end):
        if start == end:
            ans.append(''.join(arr[:]))
            return
        
        for i in range(start, end):
            arr[start], arr[i] = arr[i], arr[start]
            perm(ans, start+1, end)
            arr[start], arr[i] = arr[i], arr[start]
    ans = []
    perm(ans, 0, len(arr))
    a = sorted(set(ans))
    print(len(a))
    for e in a:
        print(e)
        

arr = list(input())
create_strings(arr)