A = {
    "1": "254",
    "2": "36541",
    "3": "652",
    "4": "12587",
    "5": "12369874",
    "6": "98523",
    "7": "854",
    "8": "74569",
    "9":"856"
}

l = []
num =0
def count(s,num):
    if len(l) == 9:
        num +=1
        return True
    for i in A[s]:
        if i not in l:
            l.append(i)
            if count(i,num):
                return True
            l.pop()

for i in range(1, 10):
    count(str(i), 0)
print(num)