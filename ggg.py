class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        N = len(s)
        strings = set()
        for i in range(N):
            remaining = s[i+1:]
            index = remaining.rfind(s[i])
            if index == -1:
                continue
            else:
                for j in range(i+1, i+index+1):
                    strings.add(s[i] + s[j] + s[i+index+1])
        return len(strings)


model = Solution()
print(model.countPalindromicSubsequence("aabca"))
