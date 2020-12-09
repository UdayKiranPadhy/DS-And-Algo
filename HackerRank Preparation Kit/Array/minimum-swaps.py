l = list(map(int,input().split()))
i = 0
count = 0
while i <len(l):
    if l[i] == i +1:
        i+=1
        continue
    l[l[i]-1],l[i] = l[i]  , l[l[i]-1]
    count +=1

print(count)