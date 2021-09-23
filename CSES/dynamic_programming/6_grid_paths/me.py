

C = 10**9 + 7
def grid_paths(n, grid):

    if grid[0][0] == '*':
        print(0)
        return
    grid[0][0] = 1
    for i in range(1,n):
        grid[0][i] = 1 if grid[0][i] != '*' and grid[0][i-1] else 0
    for i in range(1,n):
        grid[i][0] = 1 if grid[i][0] != '*' and grid[i-1][0] else 0
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] == '*':
                grid[i][j] = 0
                continue
            grid[i][j] = (grid[i-1][j]%C + grid[i][j-1]%C) % C
    print(grid[-1][-1])

n = int(input())
grid = []
for i in range(n): grid.append(list(input()))
grid_paths(n, grid)