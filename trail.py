string = input()
for i in string:
    if i in "AEIOUaeiou":
        continue
    else:
        print(i,end="")
    