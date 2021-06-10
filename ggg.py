class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

### write LinkedList class below this line ##


class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, val):
        temp = Node()
        temp.data = val
        current = self.head
        if self.head == None:
            self.head = temp
            return
        while current.next != None:
            current = current.next
        current.next = temp
    def remove(self, key):
        if self.head == None:
            return
        prev = self.head
        temp = self.head.next
        if prev.data == key:
            self.head = self.head.next
            return
        elif temp is not None and temp.data == key and temp.next is None:
            prev.next = None
            temp = None
            return
        elif temp is None or temp.next is None:
            return
        while temp.next != None and temp.data != key:
            prev = prev.next
            temp = temp.next
        if temp.data == key and temp.next!= None:
            prev.next = temp.next
            temp = None
        elif temp.data == key and temp.next == None:
            prev.next = None
        
    def Search(self, key):
        if self.head == None:
            return 'false'
        temp = self.head
        while temp.next != None and temp.data != key:
            temp = temp.next
        if temp.data == key:
            return 'true'
        return 'false'
    
    def insertIndex(self,pos,val):
        key = Node(val)
        temp = self.head
        if pos == 0:
            key.next = temp
            self.head = key
            return
        elif self.head == None:
            return
        ind = 0
        while temp.next != None and ind < pos-1:
            temp = temp.next
            ind += 1
        if ind == pos-1:
            key.next = temp.next
            temp.next = key
        else:
            return
            
    def display(self):
        l = []
        temp = self.head
        if self.head == None:
            return l
        while temp.next != None:
            l.append(temp.data)
            temp = temp.next
        l.append(temp.data)
        if len(l) == 0:
            return
        print(*l)








### write LinkedList class above this line ##

if __name__ == "__main__": 
    test_cases=int(input()) # number of test cases
    myList=LinkedList()

    while(test_cases>0):
        instruction=int(input()) # current instruction
        ####
        # 1 means insertion
        # 2 means remove value
        # 3 means search value
        # 4 means insert at particular index
        # 5 means display entire list
        ####

        if(instruction==1): 
            val=int(input())
            print(f'Insert: {val}')
            myList.insert(val)
        elif (instruction==2):
            val=int(input())
            print(f'Delete: {val}')
            myList.remove(val)
        elif (instruction==3):
            val=int(input())
            print(f'Search for {val}. Found: {myList.Search(val)}')
        elif(instruction==4):
            index=int(input())
            val=int(input())
            print(f'Insert {val} at index {index}')
            myList.insertIndex(index,val)
        elif(instruction==5):
            print('Display:')
            myList.display()
            print()
        
        test_cases=test_cases-1

        
         
           
            
        
            
            
        
            
            
        
              
             
              
        
             
        
        

        
