_, k = list(map(int, input().split()))
prices = list(map(int, input().split()))

prices.sort()
sum = 0
count = 0
for i in prices:
    sum += i
    if sum >= k:
        break
    count += 1
print(count)