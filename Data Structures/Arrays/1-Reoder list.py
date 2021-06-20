"""
If I have a list [a,b,c,d,e] how can I reorder the items in an arbitrary 
manner like [d,c,a,b,e]?

I don't want to shuffle them. I want to re-order them in a predefined manner.
(for example, I know that the 3rd element in the old list should become the 
first element in the new list)
"""

mylist = ['a', 'b', 'c', 'd', 'e']
myorder = [3, 2, 0, 1, 4]
mylist = [mylist[i] for i in myorder]
print(mylist)         # prints: ['d', 'c', 'a', 'b', 'e']