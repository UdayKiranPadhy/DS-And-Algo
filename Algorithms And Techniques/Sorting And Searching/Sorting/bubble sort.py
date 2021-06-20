_ = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            count += 1
            l[j], l[j + 1] = l[j + 1], l[j]
print(f"Array is sorted in {count} swaps")
print(f"First Element: {l[0]}")
print(f"Last Element: {l[-1]}")