# Given a sorted array of n uniformly distributed values arr[], 
# write a function to search for a particular element x in the array.

# Linear Search finds the element in O(n) time, Jump Search takes O(√ n) 
# time and Binary Search take O(Log n) time.
# The Interpolation Search is an improvement over Binary Search for instances, 
# where the values in a sorted array are uniformly distributed. Binary Search 
# always goes to the middle element to check. On the other hand, interpolation 
# search may go to different locations according to the value of the key being searched. 
# For example, if the value of the key is closer to the last element, interpolation 
# search is likely to start search toward the end side.

# To find the position to be searched, it uses following formula.

# // The idea of formula is to return higher value of pos
# // when element to be searched is closer to arr[hi]. And
# // smaller value when closer to arr[lo]
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]


def interpolationSearch(arr, n, x): 
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
    return -1
  
# Driver Code 
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, \ 
                22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 
  
if index != -1: 
    print("Element found at index",index )
else: 
    print("Element not found")




# Time Complexity: If elements are uniformly distributed, then O (log log n)). 
# In worst case it can take upto O(n).