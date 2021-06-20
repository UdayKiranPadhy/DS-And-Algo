"""
Rearrange a linked list 
Given a singly linked list, the task is to rearrange it in a way that all odd position
nodes are together and all even positions node are together.
Assume the first element to be at position 1 followed by second element at position 
2 and so on.
Example 1:
Input:
LinkedList: 1->2->3->4
Output: 1 3 2 4

Example 2:
Input:
LinkedList: 1->2->3->4->5
Output: 1 3 5 2 4
Your Task:
The task is to complete the function rearrangeEvenOdd() which rearranges the nodes 
in the linked list as required and return the head of the linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Size of the linked list <= 10000
1 <= values of linked list<= 1000
"""

def rearrangeEvenOdd(head):
    """
    Rearrange the linked list.
    """
    odd = Node(0)
    even = Node(0)
    Odds_head = odd
    Even_head = even
    isOdd = True
    while (head):
        if isOdd:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even = even.next
        isOdd = not isOdd
        head = head.next
    even.next = None
    odd.next = Even_head.next
    return Odds_head.next

def rearrangeEvenOdd2(head):
    if head == None or head.next == None:
        return head
    
    odd = head
    to_return = odd
    even = head.next
    isOdd = True
    head = head.next.next
    while head:
        if isOdd:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even = even.next
        isOdd = not isOdd
        head = head.next
    even.next = None
    odd.next = even
    return to_return



class Node: 
	def __init__(self, d): 
		self.data = d 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
		
	# A utility function to create 
	# a new node 
	def newNode(self, key): 
		temp = Node(key) 
		self.next = None
		return temp 

	# Rearranges given linked list 
	# such that all even positioned 
	# nodes are before odd positioned. 
	# Returns new head of linked List. 
	

	# A utility function to print a linked list 
	def printlist(self, node): 
		while (node != None): 
			print(node.data, end = " ") 
			node = node.next
		
	# Function to insert a new node 
	# at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

# Driver code 
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ll = LinkedList() 
        for i in range(n-1,-1,-1):
            ll.push(a[i])
        start = rearrangeEvenOdd2(ll.head) 
        ll.printlist(start) 
        print()