def isJump(number):
    num = str(number)
    for i in range(len(num)-1):
        if abs(int(num[i]) - int(num[i+1])) == 1:
            continue
        else:
            return False
    return True

l=[]
for i in range(int(input())):
    l.append(int(input()))

jumping=[]
each=[]
for i in l:
    for j in range(i):
        if isJump(j):
            each.append(j)
    jumping.extend(each)
    each.clear()
print(jumping)