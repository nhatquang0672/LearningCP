#https://atcoder.jp/contests/abc042/tasks/arc058_a
n, k = map(int, input().split())
dd = set([int(x) for x in input().split()])

def get_num(num):
    ans = set()
    while num:
        ans.add(num%10)
        num = num//10
    return ans

def sol():
    i = n
    while True:
        if not get_num(i) & dd:
            print(i)
            return
        i += 1

sol()