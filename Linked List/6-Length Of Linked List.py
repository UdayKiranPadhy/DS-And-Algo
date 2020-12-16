# Iterative Approch

def getCount(self): 
    temp = self.head # Initialise temp 
    count = 0 # Initialise count 
  
    # Loop while end of linked list is not reached 
    while (temp): 
        count += 1
        temp = temp.next
    return count
        
# Recursive Approch
def count(node):
    if node.next == None:
        return 1
    else:
        return 1 + count(node.next)