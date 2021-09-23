
occupied = []
reserved = []
ans = []
N = 8

def N_Queens(row):
    if row >= N:
        ans.append(occupied[:])
    for i in range(N):
        if is_valid(row, i, occupied) and (row, i) not in reserved:
            occupied.append((row, i))
            N_Queens(row+1)
            occupied.pop()

def is_valid(row, col, occupied):
    for r, c in occupied:
        if c == col or abs(row-r) == abs(col-c):
            return False
    return True

def print_chessboard(occupied):
    print('------------------------------------------')
    for i in range(N):
        row = ''
        for j in range(N):
            if (i, j) not in occupied:
                row += ' .'
            else:
                row += ' x'
        print(row)

for i in range(N):
    row = input()
    for j in range(N):
        if row[j] == '*':
            reserved.append((i, j))
# print(reserved)

N_Queens(0)
print(len(ans))
