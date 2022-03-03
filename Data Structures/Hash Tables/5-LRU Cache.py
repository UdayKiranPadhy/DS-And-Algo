"""

146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1 cache is {2=2 , 1 = 1}
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

Problem Statement:- https://leetcode.com/problems/lru-cache/
"""


# Solution

"""

Problem statement
https://leetcode.com/problems/lru-cache/

Solution
If O(1) complexity is not required, than it is enough to keep one dictionary and 
one array of orders of elements, which we need to update. For O(1) solution we can 
use dictionary, where we keep links to nodes of double-linked list. The idea is the following:

Keep doubly-linked list with values - for siplicity we use looped list, 
where tail is connected with head.
Keep also dictionary, where for each value we have address of corresponding 
node in our linked list.

get(self, key) will work like this: we look for our node in self.dic, remove 
it from given place and put it to the end.
put(self, key, value) will work like this: first we check if key in self.dic and 
if it is, remove it from linked list. Then we create new node, add it to the end 
and to self.dic. Also if we out of capacity, we remove head and delete it from self.dic.


Complexity
Time complexity of all operations is O(1).



"""


class Node():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cache = {}
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
