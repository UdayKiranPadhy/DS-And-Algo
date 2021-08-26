class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        max_palin = s[0]
        for i in range(len(s)):
            low = i - 1
            high = i + 1
            length = 1
            if low >= 0 and high < len(s) and s[low] == s[high]:
                length += 2
                if length > max_length:
                    max_length = length
                    max_palin = s[low:high+1]
                low -= 1
                high += 1
            
            low = i 
            high = i + 1
            length = 0
            if low >= 0 and high < len(s) and s[low] == s[high]:
                length += 2
                if length > max_length:
                    max_length = length
                    max_palin = s[low:high+1]
                low -= 1
                high += 1
        return max_palin


model = Solution()
gg = input()
print(model.longestPalindrome(gg))