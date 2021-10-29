"""

451. Sort Characters By Frequency
Medium

https://leetcode.com/problems/sort-characters-by-frequency/

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

"""

# Problem statement
# https://leetcode.com/problems/sort-characters-by-frequency/

# Solution
# We can sort pairs: (frequency, letter) using counter for all string.

# Complexity
# Time complexity in O(n + m log m), where m is size of alphabet, space complexity is O(m).

# Code
from heapq import heappop, heapify
from typing import Counter


class Solution:
    def frequencySort(self, s):
        return "".join([a*b for a, b in Counter(s).most_common()])
# Remark
# Other approaches:

# We can use counters to count frequencies of each element and put them into hash table.
# Then we can use the fact, that frequencies are never more than n and use buckets:
# for example if some letter have frequency 3, put it to bucket number 3. Then we traverse
# buckets from the end and build string. Overall time and space complexity is O(n).

# We can also use heaps instead of sort with exaclty the same complexity. In practice,
# if m is not big, performance can be better than buckets approach.

# See also similar problem 0347: Top K Frequent Elements and 0692. Top K Frequent Words.


class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        maxHeap = [[-frequency[letter], letter] for letter in frequency]
        heapify(maxHeap)
        output = ""
        while len(maxHeap):
            popedElement = heappop(maxHeap)
            output += popedElement[1]*-popedElement[0]
        return output
