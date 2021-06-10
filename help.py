from collections import deque
n = int(input())
l = deque(map(int, input().strip().split(" ")))
r = deque(map(int, input().strip().split(" ")))
# list_set = deque()
max_common_plants = 0
for i in range(len(l)):
    gg=l.pop()
    gg1=r.pop()
    starting_point = max(l)
    ending_point = min(r)
    range = ending_point - starting_point
    max_common_plants = max(max_common_plants,range)
    l.appendleft(gg)
    r.appendleft(gg1)
print(max_common_plants)