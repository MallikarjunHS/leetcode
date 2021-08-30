"""
Problem Statement: 
    Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
    return the number of negative numbers in grid.
Test Cases:
    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    [[3,2],[1,0]]
    [[1,-1],[-1,-1]]
    [[-1]]
"""

# Solution 1: 
# Time Complexity: O(n2)
# Results: Runtime: 178 ms and Memory Usage: 14.6 MB
class Solution(object):
    def countNegatives(self, grid):
        n_count = 0
        for an_item in grid:
            for i_an_item in an_item:
                if i_an_item < 0:
                    n_count = n_count+1
        return n_count

# Solution 1: 
# Results: Runtime: 136 ms and Memory Usage: 14.6 MB
class Solution2(object):
    def countNegatives(self, grid):
        n_count = 0
        row_length = len(grid[0])
        for an_item in grid:
            for i in range(row_length):
                if an_item[i] < 0:
                    n_count = n_count+(row_length-i)
                    break
        return n_count
