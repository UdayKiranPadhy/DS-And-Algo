l = [1, 5, 3, 2]
n = len(l)
count =0
for i in range(n):
    if k - l[i] in l:
        count += 1
print(count)