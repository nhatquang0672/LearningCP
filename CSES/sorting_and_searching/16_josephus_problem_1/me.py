# https://cses.fi/problemset/task/2162

def josephus_problem_1(n):        
    if n==1:
        print(1)
        return

    def get_next(arr, cur):
        run, valid = cur+1, -1
        while True:
            if run >= len(arr):
                run = 0           
            if run == cur:
                return (-1, valid)
            if valid != -1 and arr[run] != -1:
                break
            if arr[run] != -1:
                valid = run
            run += 1

        return (run, valid)

    arr = list(range(1, n+1))
    start, valid = 1, 0

    while start != -1:
        print(arr[start], end=" ")
        arr[start] = -1
        start, valid = get_next(arr, start)
    print(arr[valid])

def josephus_problem_1_version_2(n):
    # arr = list(range(1, n+1))
    # start, cur, prev =1, 1, 0
    pass

n = int(input())
josephus_problem_1(n)