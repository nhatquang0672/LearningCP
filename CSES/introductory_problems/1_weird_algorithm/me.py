# https://cses.fi/problemset/task/1068

def weird_algorithm(number):
    while number != 1:
        print(int(number), end=' ')
        number = number/2 if number%2 == 0 else number*3+1
    print(1)
if __name__ == '__main__':
    s = int(input())
    weird_algorithm(s)