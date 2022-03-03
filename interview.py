
def go():

    n  =  int(input("Enter the number of Fib number you want"))
    if n == 1 :
        print("0")
        return
    elif n == 2:
        print("0 1 ")
        return
    f1 = 0
    f2 = 1
    print(f1,end = " ")
    print(f2 , end = " ")
    while n:
        print(f1 + f2 , end = " ")
        temp = f2 
        f2 = f1 + f2
        f1 = temp
        n -= 1
    return
        
    

if __name__ == "__main__":
    go()