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

# This post is to deep dive into one of the most fundamental data structures called Heap. 
# The objective of this post is to understand the basics of Heap, time complexities, and 
# identify patterns when to use Heap as a data structure.

# Heap questions are one of the most common questions frequently asked in interviews.

# The confidence in HEAP data structure is guranteed if you finish below mentioned 23 questions.

# What is Heap?
# It is mainly used to represent a priority queue.
# It is represented as a Binary Tree (a tree structure where a node of a tree has a maximum of 
# two child nodes). Heaps are complete binary trees.
# A simple array can be used to represent a Heap where array indices refer to the node 
# position in the tree.
# Parent and child nodes can be accessed with indices:
# A root node｜i = 0, the first item of the array
# A parent node｜parent(i) = i / 2
# A left child node｜left(i) = 2i
# A right child node｜right(i)=2i+1
# Two type of Heaps — Min Heap, Max Heap
# Min Heap — the parent node always has a smaller value than the child nodes.
# Max Heap — the parent node is always larger than the child node value.
# Usually, when a type is not mentioned, it refers to the MinHeap. Python Heap has 
# minHeap as default.
# In python, theheapqmodule provides the basic features for Heap data structure.
# minHeap are used in tasks related to scheduling or assignment. A more detailed 
# explanation is under the Patterns section below.
# Heap Operations
# The basic operations in Python heapq are:

# heapify
# The heapify operation converts the iterable array heap into a tree 
# structure w.r.t heap order.

# heappush
# It inserts an element into the heap. Post insertion the heap order is 
# adjusted to maintain the heap properties.

import heapq as hq
# Simple array is heap
minHeap = []
# Adding an element to the heap
hq.heappush(minHeap, 5)
heappop
# This operation is to remove the element from the heap. By default it is minHeap, so this operation removes the min element from the minHeap. And for maxHeap, it is the maximum element. Post removal, heapify is called internally to maintain the heap order.

import heapq as hq
minHeap = [5, 6, 2]
# this is done to convert iterable into a heap tree
hq.heapify(minHeap) 
# Getting top element from the heap
value = hq.heappop(minHeap) # the value here is 2 as 2 is the minimum value. 
# Other operations in heapq python module includes heappushpop ,heapreplace , nlargest , nsmallest .

# A simple Python implementation of MIN HEAP
class MinHeap:
  """
  Min Heap Implementaion
  """
  
  def __init__(self, array):
    """Initialization method."""
      
    # Build heap. Below statement is to convert 
    # an array into heap order. This is similar to 
    # heapq.heapify
      
    self.heap = self.buildHeap(array)

  # TC O(N) | SC O(1) 
  def buildHeap(self, array):
    """Build heap from iterable"""
    
    firstParentIdx = (len(array)-2)//2
    for currentIdx in reversed(range(firstParentIdx + 1)):
      self.siftDown(currentIdx, len(array) - 1, array)
    return array

  # TC O(logN) | SC O(1) 
  def siftDown(self, currentIdx, endIdx, heap):
    """Sifting down operation moves the value successively
    down the tree if its childer has smaller value.
    This is done to maintain the heap order.
    """
    childOneIdx = (2*currentIdx) + 1
    while childOneIdx < len(heap):
      childTwoIdx = (2*currentIdx) + 2 if currentIdx*2+2 <= endIdx else -1
      if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      if heap[idxToSwap] < heap[currentIdx]:
        self.swap(currentIdx, idxToSwap, heap)
        currentIdx = idxToSwap
        childOneIdx = currentIdx * 2 +1
      else:
        break

  # TC O(logN) | SC O(1) 
  def siftUp(self, currentIdx, heap):
    """
    It is exact opposite of sift down. 
    """
    parent = (currentIdx-1)//2
    while currentIdx > 0 and heap[parent] > heap[currentIdx]:
      self.swap(parent, currentIdx, heap)
      currentIdx = parent
      parentIdx = (currentIdx-1)//2
		
  # TC O(1) | SC O(1) 
  def peek(self):
    """Get the top value of the heap.
    It returns the smallest value in min heap.
    """
    return self.heap[0]

  # TC O(logN) | SC O(1) 
  def remove(self):
    """
    Removing an element from heap. 
    This is similar to heaq.heappop
    """
    self.swap(0, len(self.heap)-1, self.heap)
    valueToRemove = self.heap.pop()
    self.siftDown(0, len(self.heap)-1, self.heap)
    return valueToRemove

  # TC O(logN) | SC O(1) 
  def insert(self, value):
    """
    Inserting an element in the heap. 
    Similar to heappush operation. 
    """
    self.heap.append(value)
    self.siftUp(len(self.heap)-1, self.heap)

  def swap(self, i, j , heap):
    """Swap two elements in an array"""
    heap[i], heap[j] = heap[j], heap[i]

# Problem Patterns where HEAP is used
# Based on my understanding, different questions where HEAP is common data structure to 
# use can be categorized in following 4 categories:

# Top K Pattern
# Merge K Sorted Pattern
# Two Heaps Pattern
# Minimum Number Pattern
# All questions under one patterns has some similarities in terms of using HEAP as a data structure. 
# Completing these questions would gurantee you mastery on the HEAP data structure. 
# Below list includes some of the most common questions asked in most of the companies.