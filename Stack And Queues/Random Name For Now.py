

def MAH(bags, b):
    left_smaller = b
    for i in R(b, -1, -1):
        if bags[i] < bags[b]:
            left_smaller = i
            break
    right_smaller = b
    for i in R(b, len(bags)):
        if bags[i] < bags[b]:
            right_smaller = i
            break
    return (right_smaller-(left_smaller+1))*bags[b]


def solve():
    n = I(input())
    bags = listInput()
    bags.insert(0, -1)
    bags.append(-1)
    coins = []
    for b in R(1, len(bags)-1):
        coins.append(MAH(bags, b))
    return max(coins)


if __name__ == '__main__':
    R = range
    I = int
    def listInput(): return [I(x) for x in input().strip().split(" ")]
    mod = 10000007
    inf = float('inf')
    for t in R(I(input())):
        print(solve())
