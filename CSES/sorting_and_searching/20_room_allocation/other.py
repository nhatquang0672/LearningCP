from sys import stdin, stdout
 
readln = stdin.readline
writelst = lambda x: stdout.write(' '.join(map(str, x)))
writenum = lambda x: stdout.write(str(x) + '\n')
writestr = lambda x: stdout.write(x)
M = 10**6
 
# solution to room allocation
def room_allocation(days, n):
    room = [0]*n
    free_rooms = []
    min_rooms = 0
    
    for day in days:
        data = day // M
        pos = day % M
        if data % 2 == 0:
            if free_rooms:
                room[pos]=free_rooms.pop()
            else:
                min_rooms += 1
                room[pos] = min_rooms
        else:
            free_rooms.append(room[pos])
    
    writenum(min_rooms)
    writelst(room)
    writestr('\n')
 
# Input data
n = int(readln())
days = []
for i in range(n):
    a, b = map(int, readln().split())
    days.append((M*(2*a))+i)
    days.append((M*(2*b+1))+i)
# Sorting list
days.sort()
# function call
room_allocation(days, n)