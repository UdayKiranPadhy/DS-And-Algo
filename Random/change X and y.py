for t in range(1):
    n = 5
    l = list(range(1, n + 1))
    subarrays = []
    for i in range(1, len(l) + 1):
        for j in range(len(l)):
            if j + i <= len(l):
                subarrays.append(l[j : j + i])
    print(subarrays)
    sum_max = 0
    sum_min = 0
    for i in subarrays:
        sum_max += max(i)
        sum_min += min(i)
    print(sum_max - sum_min)

print()

l = [1, 2, 3, 4, 5]
sum = 0
for i in range(len(l)):
    sum += l[i] * (2 ** i - 2 ** (len(l) - i))
print(sum)

l = [1, 2, 3, 4, 5]
n = len(l) - 1
sum = 0
for i in l:
    sum += i * n
    n -= 1
print(sum)

for t in range(int(input())):
    n = int(input())
    l = list(range(1, n + 1))
    n = len(l) - 1
    sum = 0
    for i in l:
        sum += i * n
        n -= 1
    print(sum)