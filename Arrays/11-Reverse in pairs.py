"""
Reverse array in groups 
Basic
Given an array arr[] of positive integers of size N. 
Reverse every sub-array group of size K. 

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
 

Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
 

Your Task:
You don't need to read input or print anything. The task is to complete the function reverseInGroups() which takes the array, N and K as input parameters and modifies the array in-place. 

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

 

Constraints:
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018

Topic Tags
 Arrays

https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1
"""


class Solution:
    def reverseInGroups(self, arr, N, K):
        aux = []
        for i in range(0, len(arr), K):
            if i + K >= len(arr):
                aux += arr[i:][::-1]
                break
            aux += arr[i : i + K][::-1]
        for i in range(N):
            arr[i] = aux[i]


model = Solution()
gg = [1, 2, 3, 4, 5]
print(model.reverseInGroups(gg, 5, 3))
print(gg)

# Hint 1
"""
Iterate over the array and keep reversing k elements at a time.
"""

# Hint 2
"""
You can take a window of size k. Now, this problem is reduced to 
reversing an array. After reversing the first group, keep going for next 
group if there are atleast k elements reverse k elements and if there are 
less than k elements left then reverse the remaining elements. 
"""

# Solution


class Solution2:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        i = 0
        while i < N:
            # If (ith index +k) is less than total number of elements it means
            # k elements exist from current index so we reverse k elements
            # starting from current index.
            if i + K < N:
                # reversed function used to reverse any part of the array.
                arr[i : i + K] = reversed(arr[i : i + K])
                # updating index from i to i+k.
                i += K

            # Else k elements from current index doesn't exist.
            # In that case we just reverse the remaining elements.
            else:
                # reversed function used to reverse any part of the array.
                arr[i:] = reversed(arr[i:])
                # updating index from i to i+k.
                i += K

# C++
"""
class Solution{
public:
    //Function to reverse every sub-array group of size k.
    void reverseInGroups(vector<long long>& arr, int n, int k){
        for(long long i = 0;i<n;i+=k){ 
            
            //If (ith index +k) is less than total number of elements it means
            //k elements exist from current index so we reverse k elements 
            //starting from current index.
            if(i+k < n){ 
                //reverse function used to reverse any part of the array.
                reverse(arr.begin()+i, arr.begin()+(i+k));
            }
            
            //Else k elements from current index doesn't exist. 
            //In that case we just reverse the remaining elements.
            else{
                //reverse function used to reverse any part of the array.
                reverse(arr.begin()+i, arr.end());
            }
        }
    }
};

"""
# Java
"""
//Back-end complete function Template for Java

class Solution{
    //Function to reverse any part of the array.
    void reverse(ArrayList<Integer> arr, int n,int left, int right)
    {
           //reversing the sub-array from left index to right index.
            while (left < right) { 
                //swapping values at index stored at left and right index.
                int temp = arr.get(left); 
                arr.set(left, arr.get(right)); 
                arr.set(right, temp);
                
                //updating values of left and right index.
                left+=1; 
                right-=1;  
            }
    }
    
    //Function to reverse every sub-array group of size k.
    void reverseInGroups(ArrayList<Integer> arr, int n, int k) {
        for (int i = 0; i < n; i += k) { 
            
            //If (ith index +k) is less than total number of elements it means
            //k elements exist from current index so we reverse k elements 
            //starting from current index.
            if(i+k < n){ 
                //reverse function called to reverse any part of the array.
                reverse(arr,n,i,i+k-1);
            }
            //Else k elements from current index doesn't exist. 
            //In that case we just reverse the remaining elements.
            else{
                //reverse function called to reverse any part of the array.
                reverse(arr,n,i,n-1);
            }
           
        }
    }
}


"""