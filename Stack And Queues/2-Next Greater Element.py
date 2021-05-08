"""
Next Greater Element 
Medium Accuracy: 48.92% Submissions: 18132 Points: 4
Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
Example 2:

Input: 
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to 
6 is 8, for 8 there is no larger elements 
hence it is -1, for 0 it is 1 , for 1 it 
is 3 and then for 3 there is no larger 
element on right and hence -1.
Your Task:
This is a function problem. You only need to complete the function nextLargerElement() that takes list of integers arr[ ] and N as input parameters and returns list of integers of length N denoting the next greater elements for all the corresponding elements in the input array.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ N ≤ 106
1 ≤ Ai ≤ 1018

Topic Tags
Stacks

"""
# Links
# https://www.geeksforgeeks.org/next-greater-element/
# https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1

"""
Method 1 (Simple) 
Use two loops: The outer loop picks all the elements one by one. The inner loop looks for the first greater element for the element picked by the outer loop. If a greater element is found then that element is printed as next, otherwise -1 is printed.
"""

# printNGE(arr)
"""
Time Complexity: O(n^2). The worst case occurs when all elements are sorted in decreasing order.

Method 2 (Using Stack) 

Push the first element to stack.
Pick rest of the elements one by one and follow the following steps in loop. 
Mark the current element as next.
If stack is not empty, compare top element of stack with next.
If next is greater than the top element,Pop element from stack. next is the next greater element for the popped element.
Keep popping from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
Finally, push the next in the stack.
After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
"""

# https://youtu.be/8P-Z7Oc8x9I
# My Trail
def nextLargerElement(arr, n):
    stack = []
    output = []
    for i in range(len(arr) - 1, -1, -1):
        if len(stack) == 0:
            output.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            output.append(stack[-1])
        elif len(stack) > 0 and stack[-1] < arr[i]:
            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])
    output.reverse()
    print(output)


nextLargerElement([98, 23, 54, 12, 20, 7, 27], 7)


# Correct Output

# Stack Functions to be used for our stack
def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()


"""
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
"""


def nextLargerElement(arr, n):

    next_greater = [-1 for i in range(n)]  # our answer list, initialized to -1.
    s = createStack()
    element = 0
    next = 0

    # push the first element to stack
    push(s, [arr[0], 0])

    # iterate for rest of the elements
    for i in range(1, n, 1):
        next = arr[i]

        if isEmpty(s) == False:

            # if stack is not empty, then pop an element from stack
            elem = pop(s)  # value, index pair popped from stack
            element = elem[0]  # get the value stored in the pair
            curr_index = elem[1]  # get the value stored in the pair

            """If the popped element is smaller than next, then 
                a) print the pair 
                b) keep popping while elements are smaller and 
                   stack is not empty """
            while element < next:
                next_greater[
                    curr_index
                ] = next  # assign value of nge to corresponding index
                if isEmpty(s) == True:
                    break
                elem = pop(s)
                element = elem[0]
                curr_index = elem[1]

            """If element is greater than next, then push 
               the element back """
            if element > next:
                push(s, [element, curr_index])

        """push next to stack so that we can find 
           next greater for it """
        push(s, [next, i])

    """After iterating over the loop, the remaining 
       elements in stack do not have the next greater 
       element, so let -1 be for them, as initialized. """

    return next_greater


# In C++
"""
vector<long long> nextLargerElement(vector<long long> arr, int n){
    stack<long long > s;
    vector<long long > res (n);
    
    for (int i = n-1; i >= 0; i--)
    {
        while (!s.empty () and s.top () <= arr[i])
            s.pop ();
            
        if (s.empty ())
            res[i] = -1;
        else 
            res[i] = s.top ();
            
        s.push (arr[i]);
    }
    return res;
}
"""
