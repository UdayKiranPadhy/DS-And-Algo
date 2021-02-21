"""
Leaders in an array 
Easy
Given an array A of positive integers. Your task is to find the leaders 
in the array. An element of array is leader if it is greater than or equal 
to all the elements to its right side. 
The rightmost element is always a leader. 

Example 1:
Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements 
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
 
Example 2:
Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0
 

Your Task:
You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 107
0 <= Ai <= 107

Company Tags
 Payu
Topic Tags
 Arrays Searching
"""
import sys


def leaders(A, N):
    max_upto_here = -sys.maxsize - 1
    l = []
    print(max_upto_here)
    for i in range(len(A) - 1, -1, -1):
        if A[i] >= max_upto_here:
            l.append(A[i])
            max_upto_here = A[i]
    return l[::-1]


# Hint 1
"""
Traverse all the elements from right to left in array and check whether 
the current element is greater than the maximum stored till now.
"""

# Hint 2
"""
1.Start iterating from the last element.

2.Check whether the current element is greater than the maximum stored till now

3.If it is greater, store the current element in a list and then update the maximum.

4.Reverse the list and return it.
"""

# Solution

"""
Python
#Function to find the leaders in the array.
def leaders(A,N):
    ans=[]
    maxx=A[N-1]

    #We start traversing the array from last element.
    for i in range(N-1,-1,-1):
        #Comparing the current element with the maximum element stored till now. 
        #If current element is greater than max we append the element.
        if A[i]>=maxx:
            #Updating the maximum element.
            maxx=A[i]
            #Appending the current element.
            ans.append(maxx)
            
    #Reversing the array.
    ans.reverse()
    #returning the answer.
    return ans


C++
vector<int> leaders(int a[], int n){
    vector<int> v;
    
    long long max = a[n-1];
    
    //We start traversing the array from last element.
    for(long long i =n-1; i >= 0; i--){
        //Comparing the current element with the maximum element stored till now. 
        //If current element is greater than max we add the element in vector.
        if(a[i] >= max){
            //Updating the maximum element.
            max = a[i];
            //Storing the current element in vector for leaders.
            v.push_back(max);
        }
    }
    //Finally reversing the vector in which leaders are stored.
    reverse(v.begin(), v.end());
    //returning the vector.
    return v;
    
}


Java
class Leader{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int arr[], int n){
        
        int maxEle = arr[n-1];
        
        ArrayList<Integer> res = new ArrayList<>();
        
        //We start traversing the array from last element.
        for(int i=n-1; i>=0; i--) {
            
            //Comparing the current element with the maximum element stored. 
            //If current element is greater than max we add element in arraylist.
		    if(arr[i] >= maxEle){
		        //Updating the maximum element.
		        maxEle = arr[i];
		        //Storing the current element in arraylist for leaders.
		        res.add(maxEle);
		    }
		}
		
		//Reversing the arraylist.
		Collections.reverse(res);
		//returning the arraylist.
        return res;
    }
    
}

"""