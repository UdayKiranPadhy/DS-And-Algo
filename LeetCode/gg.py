# l = []
# for i in range(int(input())):
#     l.append(input().split())
# for i in l:
#     count =0
#     for j in range(int(i[0]), int(i[1])+1):
#         if str(j).count(i[2]) == int(i[3]):
#             count += 1
#     print(count,end=" ")

l = []
for i in range(int(input())):
    l.append(int(input()))

for i in l:
    count = 0
    for j in range(1,i+1):
        count += int(bin(j).lstrip("0b"))
    print(count)