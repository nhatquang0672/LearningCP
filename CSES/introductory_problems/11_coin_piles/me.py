# https://cses.fi/problemset/task/1754

def coin_piles(a, b):
    if (a+b)%3 == 0 and a <= 2*b and b <= 2*a:
        print('YES')
    else:
        print('NO')

input_size = int(input())
for i in range(input_size):
    a, b = map(int, input().split())
    coin_piles(a, b)