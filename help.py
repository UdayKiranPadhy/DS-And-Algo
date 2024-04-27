from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        prev = None
        ops  = 0
        for c in range(C-1,-1,-1):
            freq = Counter()
            for r in range(R):
                freq[grid[r][c]] += 1
            if prev is not None:
                if freq.most_common(1)[0][0] == prev:
                    if len(freq) > 1:
                        ops += R - freq.most_common(2)[1][1]
                        prev = freq.most_common(2)[1][0]
                    else:
                        ops += R
                        prev = None
                else:
                    ops += R - freq.most_common(1)[0][1]
                    prev = freq.most_common(1)[0][0]
            else:
                ops += R - freq.most_common(1)[0][1]
                prev = freq.most_common(1)[0][0]
        return ops



model = Solution()
gg = [[3,5,3,6,0,9,9,2,3,3],[6,6,7,5,1,8,3,8,0,3]]
print(model.minimumOperations(gg))
