"""

372. Super Pow
Medium

367

965

Add to List

Share
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
Example 4:

Input: a = 2147483647, b = [2,0,0]
Output: 1198
 

Constraints:

1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b doesn't contain leading zeros.

"""

#Solution
# Problem Link: https://leetcode.com/problems/super-pow/

# Take a brief observation: a=2 , n=[5,4,3,2,1] We have to find 2^(54321)%1337 
# Basic Rule: (a * b)%c = (a%c * b%c )%c

# Now , 2^(54321) = 2^(54320) * 2^1

# = ((2^5432)^10) * 2^1

# = ([((2^5430) * (2^2)]^10) * 2^1
# = [ [ 2^543] ^ 10 * 2^2 ] ^ 10 * 2^1
# .
# .
# .
# =[[[(2^**5**)^10 * 2^**4** ]^10 * 2^**3** ] ^10 ] * 2^**2** ] ^ 10 * 2^**1**
# Dont forgot to use multiplication mod property , I have not added that one in explanation
# Below is the implementation of this explain

class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        def power(a,gg):
            if len(gg) == 1:
                return pow(a,int(gg),1337)
            else:
                if gg[-1] == '0':
                    return pow(power(a,gg[:len(gg)-1]),10,1337)
                else:
                    return pow(a,int(gg[-1]),1337)*power(a,gg[:len(gg)-1]+"0")%1337
        b = [str(i) for i in b]
        number = "".join(b)
        return power(a,number)

model = Solution()
print(model.superPow(2,[5,4,3,2,1]))