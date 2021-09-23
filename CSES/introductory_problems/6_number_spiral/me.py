# https://cses.fi/problemset/task/1071

def spiral_number(y, x):
    m = max(y, x)
    return m**2 - (m-1) + (y-x)*(-1)**m

t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(spiral_number(y, x))

