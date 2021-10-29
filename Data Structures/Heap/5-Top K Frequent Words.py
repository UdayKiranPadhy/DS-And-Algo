"""

692. Top K Frequent Words
Medium

3665

225

Add to List

Share
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

"""

# Problem statement
# https://leetcode.com/problems/top-k-frequent-words/

# Solution
# One solution is to use counter, put all words with their frequencies into heap and
# then extract top k: time complexity is O(n + k log n), space complexity is O(n).
# If we keep size of our heap not more than k, then complexity will be O(n log k),
# which is in fact worse than previous complexity. Note also, that here we did not
# take into account comparison of words if we have the same frequency, so complexity
# is more like O(n log k s), where s is average length of word.

# Complexity
# Time complexity is O(n*s*log k), space is O(n*s).

# Code
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k):
        cnt, res = Counter(words), []
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapq.heapify(heap)

        for _ in range(k):
            _, word = heapq.heappop(heap)
            res += [word]

        return res
# Remark
# There is also solution, using buckets, similar to problem 0347 Top K Frequent Elements,
# with complexity O(n + L) = O(ns), where L is total sum of length of words: the difficulty
# is what to do if we have words in the same bucket. We can use tries to sort words quickly
# (this is basically radix sort).


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        maxHeap = [[-frequency[word], word] for word in frequency]
        heapify(maxHeap)
        ans = []
        while k:
            ans.append(heappop(maxHeap)[1])
            k -= 1
        return ans
