# https://cses.fi/problemset/task/1092

def two_sets(num):
    total_sum = num*(num+1)//2
    if (total_sum % 2 == 1):
        print("NO")
    else:
        print("YES")
        part_sum = total_sum // 2
        first = []
        second = []
        for i in range(num, 0, -1):
            if part_sum-i > 0:
                part_sum -= i
                first.append(i)
            else:
                if i == part_sum:
                    part_sum -= i
                    first.append(i)
                else:
                    second.append(i)
        print_ans(first)
        print_ans(second)

def print_ans(arr):
    print(len(arr))
    print(' '.join([str(x) for x in arr]))

num = int(input())
two_sets(num)