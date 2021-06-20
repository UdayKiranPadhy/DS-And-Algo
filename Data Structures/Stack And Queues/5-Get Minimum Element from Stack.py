"""
You are given N elements and your task is to Implement a Stack 
in which you can get minimum element in O(1) time.

Example 1:

Input:
push(2)
push(3)
pop()
getMin()
push(1)
getMin()
Output: 3 2 1
Explanation: In the first test case for
query 
push(2)  the stack will be {2}
push(3)  the stack will be {2 3}
pop()    poped element will be 3 the
         stack will be {2}
getMin() min element will be 2 
push(1)  the stack will be {2 1}
getMin() min element will be 1
Your Task:
You are required to complete the three methods push() which take one argument an integer 'x' to be pushed into the stack, pop() which returns a integer poped out from the stack and getMin() which returns the min element from the stack. (-1 will be returned if for pop() and getMin() the stack is empty.)

Expected Time Complexity : O(1) for all the 3 methods.
Expected Auixilliary Space : O(1) for all the 3 methods.

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100

Company Tags
 Amazon D-E-Shaw FactSet Flipkart Goldman Sachs GreyOrange Kuliza Microsoft One97 SAP Labs Sapient Snapdeal Walmart
Topic Tags
 Stack

"""


"""
1. Define a variable minEle that stores the current minimum element in the stack. 
When a minEle is removed fromt he stack, we push “2x – minEle” into the stack 
instead of x so that previous minimum element can be retrieved using current minEle 
and its value stored in stack.

Push(x) : Inserts x at the top of stack.

If stack is empty, insert x into the stack and make minEle equal to x.
If stack is not empty, compare x with minEle. Two cases arise:
If x is greater than or equal to minEle, simply insert x.
If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x.
Pop() : Removes an element from top of stack.

Remove element from top. Let the removed element be y. Two cases arise:
If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
If y is less than minEle, the minimum element now becomes (2*minEle – y), update (minEle = 2*minEle – y). Now retrieve previous minimum from current minimum and its value in stack.

"""

# User function Template for python3


class stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        if len(self.s) == 0:
            self.minEle = x
        else:
            if x < self.minEle:
                self.minEle = x
        self.s.append(x)

    def pop(self):
        if len(self.s) != 0:
            return self.s.pop(-1)
        else:
            return -1

    def getMin(self):
        if len(self.s) != 0:
            return min(self.s)
        else:
            return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk = stack()

        qi = 0
        qn = 1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi + 1])
                qi += 2
            elif qt == 2:
                print(stk.pop(), end=" ")
                qi += 1
            else:
                print(stk.getMin(), end=" ")
                qi += 1
            qn += 1
        print()


# Correct Answer


class stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        if not self.s:
            self.minEle = x
            self.s.append(x)
            return
        if x < self.minEle:
            self.s.append(2 * x - self.minEle)
            self.minEle = x
        else:
            self.s.append(x)

    def pop(self):

        if not self.s:
            return -1

        top = self.s.pop()

        if top < self.minEle:
            k = self.minEle
            self.minEle = 2 * k - top
            return k
        else:
            return top

    def getMin(self):
        if not self.s:
            return -1
        else:
            return self.minEle
