def median(l):
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    return l[len(l) // 2]


print(median([1, 2, 3, 4, 5]))
