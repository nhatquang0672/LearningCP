# https://cses.fi/problemset/task/1644
from collections import deque

class MinDeque:
    def __init__(self, A, B):
        a, b = A, B
        self._data = deque([[0, 0]])

    def insert(self, val, idx):
        while self._data and self._data[-1][0] > val:
            self._data.pop()
        self._data.append([val, idx])
    
    def get(self, idx):
        while self._data and idx-self._data[0][1] > b:
            self._data.popleft()
        return self._data[0][0]
    
def maximum_subarray_sum_II(arr, n, a, b):

    ans = float('-inf')
    s = [0]*(n+1)
    md = MinDeque(a, b)
    for i in range(0, n):
        s[i+1] = s[i]+arr[i]

    for i in range(1, n+1):
        if i >= a:
            md.insert(s[i-a], i-a)
            ans = max(ans, s[i]-md.get(i))

    print(ans)            

n, a, b = map(int, input().split())
arr = [int(x) for x in input().split()]
maximum_subarray_sum_II(arr, n, a, b)

# 8 1 1
# 100 3 -2 5 3 -5 2 2
