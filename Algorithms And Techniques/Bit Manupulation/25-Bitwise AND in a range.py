"""
Problem Statement : https://leetcode.com/problems/bitwise-and-of-numbers-range/
201. Bitwise AND of Numbers Range
Medium

Given two integers left and right that represent the range [left, right], return the 
bitwise AND of all numbers in this range, inclusive.
 

Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0


Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
Accepted
171,721
Submissions
431,900

"""

# Solution Approach : https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/594464/Detailed-Python-solution-using-binary-string

"""
Idea
Bitwise AND has two properties:

ANDing same bits always results in the original bit. 1 & 1 = 1, 0 & 0 = 0.
ANDing different bits always results in zero. 1 & 0 = 0, 0 & 1 = 0.
Therefore, given two numbers m,n and their binary representation mbin, nbin, 
assumme mbin < nbin and len(mbin) == len(nbin)

The result of mbin & nbin has the same longest common prefix common as mbin and nbin (property 1).
If we AND every binary number ranging from mbin to nbin, every number in [mbin, nbin] has 
common prefix, hence the result will definitely have the common prefix.
However, the result's remaining bits are zero. Why? Every bit at remaining positions, 
regardless of their initial value, have a chance of becoming zero as we increment from 
mbin to nbin. According to property 2, every remaining position is ANDed with 0 at 
least once, so corresponding position in result will be 0

For example, given m=49, n=51, we have :
mbin = 110001, and
nbin = 110011
mbin & nbin = 110001
The longest common prefix is 1100 from m and n. 
Therefore, mbin & mbin+1, mbin+1 & nbin also has 1100 as its prefix.
result = mbin & mbin+1 & ... & nbin
= 110001 & 110010 & 110011
= 110000
1100 is still the prefix, but remaining bits are 00 since 01 & 10 & 11 = 00

What if len(mbin) != len(nbin)? If we right align mbin and nbin, we will 
see they have no common prefix, in other words len(common) == 0, so the result 
will definitely be zero.

For example, m=12, n=44 have no common prefix:
mbin=001100
nbin=101100


"""


def rangeBitwiseAnd(left: int, right: int) -> int:
    mbin = bin(left)[2:]
    nbin = bin(right)[2:]

    if len(mbin) != len(nbin):
        return 0
    else:
        count = 0
        for i, j in zip(mbin, nbin):
            if i == j:
                count += 1
            else:
                break
        res = mbin[:count] + "0" * (len(mbin) - count)
        return int(res, 2)


print(rangeBitwiseAnd(1, 7))
