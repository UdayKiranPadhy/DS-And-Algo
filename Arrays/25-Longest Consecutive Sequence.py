"""

Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


"""

# Solution
"""
so this is a pretty easy solution lets go step by step:

if we have duplicates still the chain wont be affected for 
ex 1,1,2,3,4 is still 4 in size as we so we craeate a set as 
duplicates wont affect

now see if he 1,2,3,4 now the basic idea is to start a chain from 
that no whose num-1 is not there otherwise we will start from num-1 to 
make chain bigger in size ...for eg in this case if we start at 2 but 
we see we have 2-1 already and if we start from their we get long chain 
and so we got the idea of start point

now from starting point we see how far can we get the chain thats why i 
used while loop used a count variable and at last after every iteration 
we checked for max result.

at end returned the result

we also not sorted this list nums
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        max_count = 0
        for i in numset:
            if i-1 not in numset:
                count = 1
                while (i + 1) in numset:
                    count += 1
                    i = i+1
                if count > max_count:
                    max_count = count
        return max_count