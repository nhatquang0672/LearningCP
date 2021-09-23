import sys
def get():
    return sys.stdin.readline()
arrival = list()
depart = list()
n = int(get())
 
max_count = cur_count = 0
for i in range(n):
    
    a,b = map(int,get().split())
    arrival.append(a)
    depart.append(b)
    
p1 = p2 = 0
arrival.sort()
depart.sort()
while  p1<n and p2< n :
    
    if arrival[p1]<depart[p2]:
        cur_count += 1
        p1 += 1
    elif arrival[p1]==depart[p2]:
        p1 += 1
        p2+=1
    else :
        cur_count -= 1
        p2+=1
    max_count = max(max_count,cur_count)  
 
sys.stdout.write(str(max_count)+"\n")