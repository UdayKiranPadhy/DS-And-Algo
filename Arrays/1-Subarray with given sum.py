"""
Subarray with given sum 
Easy 
Given an unsorted array A of size N that contains only non-negative integers, 
find a continuous sub-array which adds to a given number S. 

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
 
Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns a list containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return -1. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Ai <= 1010

 

Company Tags
 Amazon Facebook Google Visa
Topic Tags
 Arrays Prefix-sum Searching Sliding-window
"""


"""
We need to use Sliding window Method to solve this Problem.

Add the elements, to currsum till it is less than S. If it becomes more than S, start deleting 
elements from start in the currsum. if the currsum again becomes less than S, again start adding elements 
to it. In between also check, if the currsum becomes equal to S.
If yes, then output start and end index, else after traversing array no such solution is found, output -1.

"""
"""
The complete solution is

Maintain start and last index to store and print these values 
Iterate the complete array.
Add array elements to cuursum
If currsum becomes greater than S, then remove elements starting from start index, till it become less 
than or equal to S, and increement start.
if currsum becomes equals to S, then print the starting and last index
if the currsum never maches to S, then print -1
"""

def subArraySum(arr, n, s):
    sum = arr[0]
    start = 0
    end = 1
    while end < n:
        if sum < s:
            sum += arr[end]
            end += 1
            continue
        if sum > s:
            sum -= arr[start]
            start += 1
            continue
        if sum == s:
            return [start + 1, end]
    return -1


print(subArraySum([1, 2, 3, 7, 5], 5, 12))

"""
vector<int> subarraySum(int arr[], int n, int s){
    
    int last=0;
    int start=0;
    unsigned long long  currsum=0;
    bool flag=false;
    vector<int>res;
    for(int i=0;i<n;i++)
    {
        // sum upto current element in the array
        currsum += arr[i];
        
        // check if current sum is greater than or equal to s
        if(currsum>=s)
        {
            // take a pointer at i, named last
            last=i;
            
            // start from start till last
            // do the excluding part while s < currsum
            while(s<currsum && start<last)
            {
                // subtract the element from left, i.e, arr[start]
                currsum -= arr[start];
                ++start;
            }
            
            // now, if current sum is equal to s
            // then print the start and end index for the subarray
            if(currsum==s)
            {
                
                res.push_back(start + 1);
                res.push_back(last + 1);
                
                // flag is set to true to check that subarray exists
                flag = true;
                break;
            }
        }
    }
    
    // if no subarray found, print -1
    if(flag==false)
        res.push_back(-1);
    
    return res;    
    
}

"""

# Java
"""
class Subarray{

    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) {
        int first = 0;
        int last = 0;

        long result = arr[first];
        ArrayList<Integer> res = new ArrayList<Integer>();
        while (result != s) {
            if (result > s) {
                if (first == last) {
                    last++;
                    first++;
                    if (last >= n) break;
                    result = arr[first];
                } else {
                    result -= arr[first];
                    first++;
                }
            } else {
                last++;
                if (last < n) {
                    result += arr[last];
                } else {
                    break;
                }
            }
        }

        if (result != s) {
            res.add(-1);
        } else {
            res.add(first + 1);
            res.add(last + 1);
            
        }
        return res;    
    }
}

"""