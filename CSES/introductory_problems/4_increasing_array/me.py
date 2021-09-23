#https://cses.fi/problemset/task/1094

def increasing_array(num, arr):
    ans, lst = 0, 0
    for ele in arr:
        lst = max(lst, ele)
        ans += lst-ele
    print((ans))        

if __name__ == '__main__':
    num = int(input())
    arr = [int(x) for x in input().split(" ")]
    increasing_array(num, arr)