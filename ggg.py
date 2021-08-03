class Solution:
    def trap(self, height: list[int]) -> int:
        N = len(height)

        def NGER(height):
            stack = [-1] * N
            maximum = -1
            for i in range(N-1, -1, -1):
                stack[i] = maximum
                if height[i] > maximum:
                    maximum = height[i]
            return stack

        def NGEL(args):
            stack = [-1] * N
            maximum = -1
            for i in range(N):
                stack[i] = maximum
                if height[i] > maximum:
                    maximum = height[i]
            return stack

        right = NGER(height)
        left = NGEL(height)
        # print(right, left)
        trap = 0
        for i in range(1, N-1):
            if right[i] > height[i] and left[i] > height[i]:
                trap += (min(right[i], left[i]) - height[i])
        return trap


model = Solution()
model.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
