"""

23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""

# Solution
# There are a bunch of different solutions for this problem, let us discuss solution,
# using heaps here. We need to iterate over k lists and on each step to choose the
# minimum element among k candidates, think of it as extention of classical merge
# stage in merge sort. If each time we find this minimum element, using lists,
# overall complexity will be O(nk), where n is total number of elements in all lists.
# However we can do better: we create heap with the following tuples as elements:

# 1) First value of tuple is our value of nodes, because we want to sort using these values
# 2) Second value of tuple is index in lists, form where we choose this element.
# Why we need this? Because when we will merge this element, we need to go to the next element
# in the corresponding list.
# Now, let us discuss main steps of algorithm:

# 1) Create dummy node in linked list, which will help us to deal with border cases,
# such as empty lists and so on.
# 2) curr is current element in linked list where are in now.
# 3) Put all starts of k linked lists to heap (actually there can be less than k,
# because some of lists can be empty)
# 4) Extract val, ind element from our heap: it will be current minumum element,
# and attach it to the end of constucted merged least so far, move curr iterator to the right.
# 5) If we still did not reach the end of current list, move one step to the
# right in this list and put new candidate to heap.
# 6) Return dummy.next.
# Complexity: time complexity is O(n log k), because we have O(n) steps, where we put
# and remove from heap, which have at most k elements. Space complexity is O(n): because
# we need to return newly constructed linked list.

# Definition for singly-linked list.
from heapq import heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        dummy = curr = ListNode(0)
        heap = []
        for ind, el in enumerate(lists):
            if el:
                heappush(heap, (el.val, ind))

        while heap:
            val, ind = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[ind].next:
                lists[ind] = lists[ind].next
                heappush(heap, (lists[ind].val, ind))

        return dummy.next
