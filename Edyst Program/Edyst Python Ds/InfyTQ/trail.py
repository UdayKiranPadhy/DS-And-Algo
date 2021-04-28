words=[]
def toString(List): 
    return ''.join(List) 
 
def permute(a, l, r): 
    if l==r: 
        words.append((toString(a)))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
# para = input()
letters=input().split(" ")
n=len(letters)
permute(letters,0,n-1)
print(words)