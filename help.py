def profit(stocks):
    mini = 0
    while mini < len(stocks)-1 and stocks[mini] >= stocks[mini+1]:
        mini += 1
    if mini == len(stocks)-1:
        return -1
    to_return = [mini]
    increasing = True
    for i in range(mini+1, len(stocks)):
        if increasing:
            if i+1 < len(stocks) and stocks[i] <= stocks[i+1]:
                continue
            else:
                to_return.append(i)
                increasing = False
        else:
            if i+1 < len(stocks) and stocks[i] >= stocks[i+1]:
                continue
            else:
                to_return.append(i)
                increasing = True
    return to_return


n = int(input())
stocks = [int(x) for x in input().strip().split(" ")]

gg = profit(stocks)
if gg == -1:
    print("Can't make a profit!")
else:
    if len(gg) % 2 != 0:
        gg.pop()
    for i in range(0, len(gg), 2):
        print(gg[i], gg[i+1])
