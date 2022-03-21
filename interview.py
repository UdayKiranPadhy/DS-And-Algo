Q1. Given a binary tree with N nodes, in which each node value represents the number of coins present at that node, and there are N coins in total. In one move, one may choose two adjacent nodes and move one candy from one node to another.
The task is to find the number of moves required such that every node has exactly one coin.


Ex: I/p:
    0
3       0

o/p: 3


Ex: I/p:
          0
    3          0                                                         2+1+1+1
    
0       0  0          1

O/p = 7

def findMaxSteps(root):
    if root == None:
        return -1
    rem = 0
    extra = 0
    
    def dfs(node):
        if node == None:
            return
        if node.val == 0:
            rem += 1
        else:
            extra = node.val - 1
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    
    if extra == rem:
        return 1 + extra
    else:
        return -1
        
        
        
        
Q2. Design a data structure that supports the following operations in Θ(1) time.
insert(x): Inserts an item x to the data structure if not already present.
remove(x): Removes item x from the data structure if present. 
search(x): Searches an item x in the data structure.
getRandom(): Returns a random element from current set of elements 


Ex:
    
    INSERT 3   {3:None}
    INSERT 4    {3:None,4:
    REMOVE 5 - 200 OK
    INSERT 6
    SEARCH 5 ---False
    GETRANDOM
    
    
    
3 4 7 8 


class DataStructure:
    def __init__(self):
        self.map = {}
        self.arr = [None]*10000
        self.index = 0
        self.empty = []
        
    def insert(val):
        if val not in self.map:
            self.map[val]= self.index
            self.arr[self.index] = val
            index+= 1
    
    def remove(val):
        if val in self.map:
            popedIndex = self.map[val]
            self.map.pop(val)
            self.arr[popedIndex] = self.arr[self.index]
            self.index -= 1
    
    def search(val):
        if val in self.map:
            return True
        else:
            return False
    def getRandom():
        number = random.randint(0,self.index)
        return self.arr[number]
        