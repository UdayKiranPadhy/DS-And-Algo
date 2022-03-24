"""

991. Broken Calculator
Medium

1494

167

Add to List

Share
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

 

Example 1:

Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
 

Constraints:

1 <= x, y <= 109


"""

# https://leetcode.com/problems/broken-calculator

# Let us consider several cases and understand, what will be the best choise 
# in each of them. Let us go in opposite direction and divide Y by 2 or add 1, 
# to it until we get X.

# If X > Y, we do not have a lot of choice, we can just decrease X by one until 
# it becomes equal to Y, so answer will be X - Y.
# If X == Y, then we already happy and we return 0.
# If Y % 2 == 1, then let us think, what can be the last step? It can not be 
# multilication by 2, so the only choice is subtraction of 1 and on previous 
# step we have configuration (X, Y + 1), for which we run our function recursively.
# If Y % 2 == 0, let us prove that we always need to divide by 2 in this case.
# Imagine, that we have sequence of operations, like: [+1, +1, /2, /2, /2, +1, /2, ...]. 
# Then, if we have +1, +1, /2 sequence inside, we can always replace it with /2, +1, so 
# we can make it shorter. So, there will be no +1, +1 subsequence, except for the 
# very end and in general all sequence looks 
# like: [+1, /2, .., /2, +1, /2, ..., /2, ..., +1, ..., +1]. Note, that the 
# last part correspondes to case 1. Also we will never have two +1 in the 
# middle and it means, that if we have even number, we must divide it by 2: if we add 1 
# to it, then we have no choice to add 1 again (case 3) and then we have +1, +1, /2 pattern.

# Complexity: time complexity is O(log Y), because every two iteration number decreased 
# at least twice. Space complexity here is also O(log Y), because we use recursion. It 
# can be made O(1) if we do it iteratively.

class Solution:
    def brokenCalc(self, X, Y):
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1