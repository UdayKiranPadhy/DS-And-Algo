from typing import List

from numpy import take


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        i = 0
        j = len(tasks) - 1
        ans =0
        while i <= j:
            current = 0
            while i <= j and  current + tasks[i] + tasks[j] <= sessionTime:
                current+= tasks[i] + tasks[j]
                i+=1
                j-=1
            while i<=j and current + tasks[j] <= sessionTime:
                current += tasks[j]
                j-=1
            ans +=1
        return ans