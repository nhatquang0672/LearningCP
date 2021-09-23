# https://cses.fi/problemset/task/1625/

N = 7

directions = "URDL"
xd = [-1, 0, 1, 0]
yd = [0, 1, 0, -1]
visited = [[False]*N for _ in range(N)]
visited[0][0] = True
path = input()
ans = 0

def is_valid(x, y):
    return x>=0 and x<N and y>=0 and y<N and not visited[x][y]

def match(cur_direction, count):
    return path[count] == '?' or path[count] == cur_direction

def grid_path(cnt, x, y):

    global ans

    if x == 6 and y == 0:
        if cnt >= N**2 -1:
            ans += 1
        return        

    t1 = is_valid(x-1, y) + is_valid(x+1, y)
    t2 = is_valid(x, y+1) + is_valid(x, y-1)
    if (t1 == 0 and t2 == 2) or (t1 == 2 and t2 == 0):
        return
    
    for i, c in enumerate(directions):
        x_new, y_new = x + xd[i], y + yd[i]
        if is_valid(x_new, y_new) and match(c, cnt):
            cnt += 1
            visited[x_new][y_new] = True
            grid_path(cnt, x_new, y_new)
            cnt -= 1
            visited[x_new][y_new] = False
      

grid_path(0, 0, 0)
print(ans)