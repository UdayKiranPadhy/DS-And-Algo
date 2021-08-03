class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        count = 0

        def LCS(string1: str, string2: str, m: int, n: int, found) -> int:
            nonlocal count

            if found == 0:
                count += 1
                return
            elif m == 0:
                return
            elif n == 0:
                return
            elif string1[m - 1] == string2[n - 1]:
                LCS(string1, string2, m - 1, n - 1, found - 1)
                LCS(string1, string2, m - 1, n - 1, found)
            else:
                LCS(string1, string2, m - 1, n, found)
                LCS(string1, string2, m, n - 1, found)

        LCS(s, t, len(s), len(t), min(len(s), len(t)))
        return count


model = Solution()
print(model.numDistinct("babgbag", "bag"))
