"""

5757. Get Biggest Three Rhombus Sums in a Grid
User Accepted:99
User Tried:221
Total Accepted:99
Total Submissions:292
Difficulty:Medium
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 105


"""


class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        
        
        def is_safe(i,j,k,l):
            nonlocal grid
            if i <len(grid) and j <len(grid[0]) and k >0 and l > 0:
                return True
            return False


        def areas(grid,i,j):
            temp_i = i, temp_j = j
            output=[]
            output.append(grid[i][j])
            for k in range(len(grid)):
                sum = 0
                if is_safe(i+k,j+k,i-k,j-k):
                    for x in range(k):
                        temp_i -=1
                        temp_j +=1
                        sum += grid[temp_i][temp_j]
                    for x in range(k):
                        temp_i +=1
                        temp_j +=1
                        sum += grid[temp_i][temp_j]
                    for x in range(k):
                        temp_i +=1
                        temp_j -=1
                        sum += grid[temp_i][temp_j]
                    for x in range(k):
                        temp_i -= 1
                        temp_j -= 1
                        sum += grid[temp_i][temp_j]
                    sum += grid[i][j]
                    output.append(sum)
                else:
                    break
            return output
        area_matrix=grid[:]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area_matrix[i][j] = max(areas(grid,i,j))
        maximums = []
        for i in range(len(grid)):
            maximums.append(max(area_matrix[i]))
        maximums.sort()
        return maximums[len(maximums)-3:len(maximums)]