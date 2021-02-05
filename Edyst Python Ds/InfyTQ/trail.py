n=input()
num = [int(i) for i in n if i.isdigit()]
num=list(set(num))
num.sort()
k=-1
for i in range(len(num)):
    if num[i]%2==0:
        k=i
        break
if k==-1:
    print(-1)
elif num[0]%2==0:
    num=num[::-1]
    print(''.join([str(i) for i in num]))
else:
    num[0],num[k]=num[k],num[0]
    num=num[::-1]
    print(''.join([str(i) for i in num]))
