"""
Polynomial Addition 

Given two polynomial numbers represented by a linked list. 
The task is to complete the function addPolynomial() that adds these 
lists meaning adds the coefficients who have the same variable powers.
Note:  Given polynomials are sorted in decreasing order of power.

Example 1:
Input:
LinkedList1:  (1,x2) 
LinkedList2:  (1,x3)
Output:
1x^3 + 1x^2
Explanation: Since, x2 and x3 both have
different powers as 2 and 3. So, their
coefficient can't be added up.

Example 2:
Input:
LinkedList1:  (1,x3) -> (1,x2)
LinkedList2:  (3,x3) -> (4,x2)
Output:
4x^3 + 6x^2
Explanation: Since, x3 has two different
coefficients as 3 and 1. Adding them up
will lead to 4x3. Also, x2 has two
coefficients as 4 and 2. So, adding them
up will give 6x2.
Your Task:
The task is to complete the function addPolynomial() which should add the 
polynomial with same powers return the required polynomial in decreasing 
order of the power in the form of a linked list.
Note: Try to solve the question without using any extra space.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N, M <= 10^5
1 <= x, y <= 10^6
"""
# Seing the time complexity we can note that we need to modify the merge function of
# Merge sort

def addPolynomial(poly1, poly2):
    to_return=poly1
    prev = poly1
    while poly1 and poly2:
        if poly1.power == poly2.power:
            poly1.coef = poly1.coef + poly2.coef
            prev = poly1
            poly1 = poly1.next
            poly2 = poly2.next
            continue
        if poly1.power > poly2.power:
            prev = poly1
            poly1 = poly1.next
        if poly2.power > poly1.power:
            prev.next = poly2
            prev = prev.next
            poly2 = poly2.next
            prev.next = poly1
    return to_return


class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    k=0
    for i in range(n):
        lis.insert(arr[k], arr[k+1])
        k+=2
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = createList(arr, n)
        sum = addPolynomial(poly1, poly2)
        ptr = sum
        while ptr is not None:
            print(str(ptr.coef) + 'x^' + str(ptr.power), end = '')
            ptr = ptr.next
            if ptr is not None:
                print(' +', end = ' ')
        print()