Y = 5
answer = 0
dp = [[[-1 for _ in range(18 + 1)] for __ in range(18 * 9 + 1)] for ___ in range(2)]


def count(num, n, sum, tight):
    global dp
    global Y
    global answer
    if sum == Y:
        answer += 1
        return 1
    elif sum > Y:
        return 0
    elif n >= len(str(num)):
        return 0
    upper_bound = 9 if not tight else int(str(num)[n])
    for i in range(0, upper_bound + 1):
        count(num, n + 1, sum + i, (tight and (i == upper_bound)))


count(15, 0, 0, 1)
print(answer)
