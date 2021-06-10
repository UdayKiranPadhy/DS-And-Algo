from collections import deque
n = int(input())
l = list(map(int, input().strip().split(" ")))
r = list(map(int, input().strip().split(" ")))
list_set = deque()
max_common_plants = 0
for x, z in zip(l, r):
    gg = set()
    for i in range(x, z+1):
        gg.add(i)
    list_set.append(gg)
del l, r
for i in range(len(list_set)):
    poped_set = list_set.popleft()
    gg = list_set[0]
    for j in range(1, len(list_set)):
        gg = gg.intersection(list_set[j])
    max_common_plants = max(max_common_plants, len(gg))
    list_set.append(poped_set)
print(max_common_plants)


# from collections import deque
# n = int(input())
# l = deque(map(int, input().strip().split(" ")))
# r = deque(map(int, input().strip().split(" ")))
# # list_set = deque()
# max_common_plants = 0
# for i in range(len(l)):
#     gg = l.pop()
#     gg1 = r.pop()
#     starting_point = max(l)
#     ending_point = min(r)
#     range = ending_point - starting_point
#     max_common_plants = max(max_common_plants, range)
#     l.appendleft(gg)
#     r.appendleft(gg1)
# if max_common_plants != 0:
#     print(max_common_plants+1)
# else:
#     print(0)
