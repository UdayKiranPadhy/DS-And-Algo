"""
A Heap is a special Tree-based data structure in which the tree is a 
complete binary tree. Generally, Heaps can be of two types:

Max-Heap: In a Max-Heap the key present at the root node must be greatest 
among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary 
Tree.

Min-Heap: In a Min-Heap the key present at the root node must be minimum 
among the keys present at all of it’s children. The same property must be 
recursively true for all sub-trees in that Binary Tree.

A Binary Heap is a Binary Tree with following properties.
1) It’s a complete tree (All levels are completely filled except possibly the 
last level and the last level has all keys as left as possible). 
This property of Binary Heap makes them suitable to be stored in an array.

2) A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the 
key at root must be minimum among all keys present in Binary Heap. The same 
property must be recursively true for all nodes in Binary Tree. 
Max Binary Heap is similar to MinHeap.

Examples of Min Heap:

            10                      10
         /      \               /       \  
       20        100          15         30  
      /                      /  \        /  \
    30                     40    50    100   40

How is Binary Heap represented?
A Binary Heap is a Complete Binary Tree. A binary heap is typically represented as an array.

The root element will be at Arr[0].
Below table shows indexes of other nodes for the ith node, i.e., Arr[i]:
Arr[(i-1)/2]	Returns the parent node
Arr[(2*i)+1]	Returns the left child node
Arr[(2*i)+2]	Returns the right child node
The traversal method use to achieve Array representation is Level Order


Applications of Heaps:
1) Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.

2) Priority Queue: Priority queues can be efficiently implemented using Binary 
Heap because it supports insert(), delete() and extractmax(), decreaseKey() 
operations in O(logn) time. Binomoial Heap and Fibonacci Heap are variations 
of Binary Heap. These variations perform union also efficiently.

3) Graph Algorithms: The priority queues are especially used in Graph 
Algorithms like Dijkstra’s Shortest Path and Prim’s Minimum Spanning Tree.

4) Many problems can be efficiently solved using Heaps. See following for example.
a) K’th Largest Element in an array.
b) Sort an almost sorted array/
c) Merge K Sorted Arrays.

Operations on Min Heap:
1) getMini(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).

2) extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Logn) as this 
operation needs to maintain the heap property (by calling heapify()) after removing root.

3) decreaseKey(): Decreases value of key. The time complexity of this operation is O(Logn). 
If the decreases key value of a node is greater than the parent of the node, then we don’t need to do anything. 
Otherwise, we need to traverse up to fix the violated heap property.

4) insert(): Inserting a new key takes O(Logn) time. We add a new key at the end of the tree. IF new key is 
greater than its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the 
violated heap property.

5) delete(): Deleting a key also takes O(Logn) time. We replace the key to be deleted with minum infinite 
by calling decreaseKey(). After decreaseKey(), the minus infinite value must reach root, so we call 
extractMin() to remove the key.
"""
from heapq import heapify,heappop,heappush,heapreplace

l=[9,6,8,3,5,1]
heapify(l)
# print(l)
# 1,3,8,6,5,9
