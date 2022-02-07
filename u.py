def helper(i,j,a:str,b:str):
    if i == len(a) and j== len(b):
        return True
    elif j == len(b):
        for letter in a[i:]:
            if letter.isupper():
                return False
        return True
    elif i == len(a):
        return False
    elif a[i].isupper() and a[i] != b[j]:
        return False
    elif a[i].isupper() and a[i] == b[j]:
        return helper(i+1,j+1,a,b)
    elif a[i].islower() and a[i].upper() == b[j]:
        # Increment both the pointers case considering we have captilized the a pointer
        op1 = helper(i+1,j+1,a,b) 

        # Increment the a str pointer hoping there is a captial b[j] in A later
        op2 = helper(i+1,j,a,b)

        return op1 or op2
    elif a[i].islower() and a[i].upper() != b[j]:
        return helper(i+1,j,a,b)
    
    


def abbreviation(a, b):
    
    if helper(0,0,a,b):
        return "YES"
    return "NO"

print(abbreviation("beFgH","EFH"))