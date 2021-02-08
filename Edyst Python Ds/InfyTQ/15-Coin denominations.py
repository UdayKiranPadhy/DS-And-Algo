k=int(input())
l=[1000, 500, 100, 50, 20, 10, 5, 2,1]
count=0
while k!=0:
    if k>=1000:
        k=k-1000
        count+=1    
    elif k>=500:
        k=k-500
        count+=1
    elif k>=100:
        k=k-100
        count+=1
    
    elif k>=50:
        k=k-50
        count+=1
    
    elif k>=20:
        k=k-20
        count+=1
    elif k>=10:
        k=k-10
        count+=1
    elif k>=5:
        k=k-5
        count+=1
    elif k>=2:
        k=k-2
        count+=1
    elif k>=1:
        k=k-1
        count+=1
print(count)