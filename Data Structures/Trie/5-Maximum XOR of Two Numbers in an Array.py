"""

421. Maximum XOR of Two Numbers in an Array
Medium

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], 
where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 2^31 - 1

"""

# https://youtu.be/I7sUjln2Fjw

from collections import defaultdict
from typing import DefaultDict, List


class Trie:
    def __init__(self) -> None:
        self.root = DefaultDict()

    def insert(self, word):
        curr = self.root
        for letter in word:
            curr = curr.setdefault(letter, defaultdict())

    def findXOR(self, word):
        gg = ""
        curr = self.root
        for letter in word:
            if letter == "0":
                if "1" in curr:
                    gg += "1"
                    curr = curr["1"]
                else:
                    gg += "0"
                    curr = curr["0"]
            else:
                if "0" in curr:
                    gg += "1"
                    curr = curr["0"]
                else:
                    gg += "1"
                    curr = curr["1"]
        return gg


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        binaries = [bin(num)[2:] for num in nums]
        max_length = max(len(i) for i in binaries)
        binaries = [i.rjust(max_length, "0") for i in binaries]
        for word in binaries:
            trie.insert(word)
        return max([int(trie.findXOR(num), 2) for num in binaries])


model = Solution()
model.findMaximumXOR([3, 5, 1, 4, 66, 7, 100])
