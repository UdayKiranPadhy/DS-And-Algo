for t in range(int(input())):
    gg = int(input())
    binary = bin(gg)[2:]
    gg = binary.rjust(32,"0")
    gg1= []
    for i in range(len(gg)):
        if gg[i] == '0':
            gg1.append('1')
        else:
            gg1.append('0')
    print(int("".join(gg1),2))