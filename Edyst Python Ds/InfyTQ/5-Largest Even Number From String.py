"""
Take as input a string. This string is a mixture of letters, integers and special char. 
From this string, find the largest even number that can pe possibly formed after removing the duplicates.
If an even is not formed then return -1.

Example Input
infosys@337

Output
-1

Explanation

No even number can be formed

Example Input
Hello#81@21349

Output
984312

"""
k=input()
l=[]
even_conists=False
for i in k:
    if i.isdigit():
        if int(i) not in l:
            l.append(int(i))
            if int(i)%2==0:
                even_conists=True
if even_conists:
    l.sort(reverse=True)
    if l[len(l)-1]%2==0:
        print("".join([str(ele) for ele in l]))
    else:
        right=len(l)-1
        while right>=0:
            if l[right]%2==0:
                l[right],l[len(l)-1]=l[len(l)-1],l[right]
                break
            right-=1
        print("".join([str(ele) for ele in l]))
else:
    print("-1")