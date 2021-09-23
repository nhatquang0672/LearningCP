from bisect import bisect_right
input()
*tickets,=map(int,input().split())
*customers,=map(int,input().split())
cnt = list(range(tickets.__len__() + 1))
tickets.sort()
for i in customers:
    old_pos = pos = bisect_right(tickets,i)
    while pos != cnt[pos]:
        pos = cnt[pos]
    while old_pos != pos:
        cnt[old_pos], old_pos = pos, cnt[old_pos]
    if pos:
        print(tickets[pos - 1])
        cnt[pos] = pos - 1
    else:
        print('-1')
    print(cnt)
