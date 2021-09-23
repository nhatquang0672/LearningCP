# https://cses.fi/problemset/task/1631/


def reading_books(n, arr):
    s = sum(arr)
    print(s if arr[-1] <= s - arr[-1] else 2 * arr[-1])
        

n = int(input())
arr = [int(x) for x in input().split(' ')]
arr.sort()
reading_books(n, arr)