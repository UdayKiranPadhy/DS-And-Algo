
"""
You are given as input a string instr, which contains only parentheses: ( ) { } [ ]. instr will have many such brackets, nested in each other. Your task is to find out if they are balanced or not.

If instr is properly balanced print 0
If instr is not properly balanced, then print the initial index where it is unbalanced
Note that indexes start from 1
Example Input
{([])}[]

Output
0

Explanation
String is balanced

Example Input
([)()]

Output
3

Explanation
First unbalanced bracket occurs at position 3

Example Input
[[()]

Output
6

Explanation
String is balanced except for last position. We need to add a closing bracket at position 6.
"""

k=input()
stack=[]
closing={
    '[':']',
    '{':'}',
    '(':')'
}
count=0
for i in k:
    count+=1
    if i in "[({":
        stack.append(i)
    if i in "])}":
        if len(stack)!=0:
            braket=stack.pop()
            if closing[braket]==i:
                continue
            else:
                print(count)
                break
        else:
            print(count)
            break
else:
    if len(stack)==0:
        print(0)
    else:
        print(count+1)