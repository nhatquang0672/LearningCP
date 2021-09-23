# https://cses.fi/problemset/task/1070

def permutations(number):
    if number == 2 or number == 3:
        print("NO SOLUTION")

    else:
        for i in range(2, number+1, 2):
            print(i, end=' ')        
        for i in range(1, number+1, 2):
            print(i, end=' ')


if __name__ == '__main__':
    s = int(input())
    permutations(s)