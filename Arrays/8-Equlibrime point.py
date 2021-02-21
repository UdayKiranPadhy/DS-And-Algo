"""
Equilibrium Point 
Easy 
Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the 
sum of elements after it.

Example 1:
Input:
n = 1
A[] = {1}
Output: 1
Explanation: Since its the only 
element hence its the only equilibrium 
point. 

Example 2:
Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case 
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2).
 

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters 
and returns the point of equilibrium. Return -1 if no such point exists.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
1 <= A[i] <= 108

Company Tags
 Adobe Amazon
Topic Tags
 Arrays Prefix-sum
"""
# My Trail
def equilibriumPoint(A, N):
    if len(A) == 1:
        return 1
    for i in range(len(A) - 1):
        if sum(A[:i]) == sum(A[i + 1 :]):
            return i + 1
    return -1


# print(equilibriumPoint([1,3,5,2,2],5))

# Time limit exceeded .Need to go for prefix-sum algo to solve it
def equilibriumPoint2(A, n):
    print(A)
    for i in range(1, len(A)):
        A[i] = A[i] + A[i - 1]
    print(A)
    for j in range(len(A) - 1, 0, -1):
        if A[len(A) - 1] - A[j] == A[j - 1]:
            return j + 1
    return -1

print(
    equilibriumPoint2([27, 4, 25, 6, 6, 1, 27, 22, 19, 29, 6, 9, 36, 24, 6, 15, 5], 5)
)


# Hint 1
"""
1.Use nested loops.

2.Outer loop iterates through all the element and inner loop finds out whether the current index picked by the outer loop is equilibrium index or not.

3.It compares the sum  of element in the left and right side of the current index.

4.Then return the equilibrium index. If it is not present, return -1.
"""

# Hint 2
"""
Tricky and Efficient Approach

1) Initialize leftsum  as 0.
2) Get the total sum of the array as sum.
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
    b) If leftsum is equal to sum, then return current index. 
    c) Else, update left sum.
        leftsum = leftsum + arr[i]
4)  If we come out of loop without returning then there is no equilibrium index return -1.
"""


# Solution
"""
def equilibriumPoint(A, N):

    #We store the sum of all array elements.
    sum = 0
    for i in range(0, N):
        sum += A[i]

    #sum2 is used to store prefix sum.
    sum2 = 0

    for i in range(0, N, +1):
        
        #Leaving out the value of current element from suffix sum.
        sum -= A[i]
        
        #Checking if suffix and prefix sums are same.
        if sum2 == sum:
            #returning the index or equilibrium point.
            return (i + 1)
        
        #Adding the value of current element to prefix sum.   
        sum2 += A[i]
        
    return -1
"""

# C++
"""
int equilibriumPoint(long long a[], int n) {

    //We store the sum of all array elements.
    long long sum = 0;
    for (int i = 0; i < n; i++) 
       sum += a[i];

    //sum2 is used to store prefix sum.
    long long sum2 = 0;
    int ans = -1;
    for (int i = 0; i < n; i++) {
        
        //Leaving out the value of current element from suffix sum.
        sum = sum - a[i];
        
        //Checking if suffix and prefix sums are same.
        if (sum2 == sum) {
            //returning the index or equilibrium point.
            return (i + 1);
        }
        
        //Adding the value of current element to prefix sum.
        sum2 = sum2 + a[i];
    }
    return -1;
}

"""