"""
https://www.geeksforgeeks.org/minimum-number-of-towers-required-such-that-every-house-is-in-the-range-of-at-least-one-tower/

Minimum number of towers required such that every house is in the range of at least one tower
Difficulty Level : Medium

Given a map of the city and the network range, the task is to 
determine the minimum number of the tower so that every house is within 
range of at least one tower. Each tower must be installed on 
top of an existing house.
Examples: 
 

Input: range : 1
       house : 1 2 3 4 5
Output: 2
All cities can be covered by inserting 2 towers i.e. at houses 2 and 4.

Input: range : 2
       house : 7 2 4 6 5 9 12 11 
Output: 3

All cities can be covered by inserting 3 towers i.e. at house 4, 9, and 12.
Algorithm:- 
 

First, sort all the elements.
Count only once and then traverse till its middle house.
After this again traverse till tower range.
Again repeat 1, 2, 3 steps till all the houses are covered.
Below is the implementation of above approach: 

"""

def number_of_tower(house, r, n):
    # first we sort the house numbers
    house.sort()
    # for count number of twoers
    numOfTower = 0
    # for iterate all houses
    i = 0
    while (i < n):
        # count number of towers
        numOfTower += 1
        # find find the middle location
        loc = house[i] + r

        # traverse till middle location
        while (i < n and house[i] <= loc):
            i += 1

        # this is point to middle
        # house where we insert the tower
        i -= 1

        # now find the last location
        loc = house[i] + r

        # traverse till last house
        # of the range
        while (i < n and house[i] <= loc):
            i += 1

    # return the number of tower
    return numOfTower


# Driver code
if __name__ == "__main__":

    # given elements
    house = [7, 2, 4, 6, 5, 9, 12, 11]
    r = 2
    n = len(house)

    # print number of towers
    print(number_of_tower(house, r, n))
