# https://cses.fi/problemset/task/1083

def missing_number(num, arr):
    sum = num*(num+1)//2
    for ele in arr:
        sum -= ele
    print(sum)

if __name__ == '__main__':
    num = int(input())
    arr = [int(x) for x in input().split(" ")]
    missing_number(num, arr)