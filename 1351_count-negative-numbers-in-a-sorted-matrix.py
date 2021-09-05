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

# Approach 1: 
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

# Approach 2: 
# Results: Runtime: 136 ms and Memory Usage: 14.6 MB
# We know 
# 1) Matrix elements are sorted 
# 2) no need to traverse all elements once encounter +/- number.
class Solution2(object):
    def countNegatives(self, grid):
        n_count = 0
        row_length = len(grid[0])
        for grid_row in grid:
            for col_num in range(row_length):
                if grid_row[col_num] < 0:
                    n_count = n_count+(row_length-col_num)
                    break
        return n_count

# Approach 3: Implements the Binary Search.
# Results: 
#   Runtime: 
#       92 ms, faster than 91.33% of Python online submissions 
#       for Count Negative Numbers in a Sorted Matrix.
#   Memory Usage: 
#       14.5 MB, less than 87.00% of Python online submissions for Count
#       Negative Numbers in a Sorted Matrix.
class Solution3(object):
    def countNegatives(self, grid):
        negative_num_count = 0
        if(len(grid) == 0):
            return negative_num_count
        for i_array in grid:
            if i_array[-1] >= 0:
                continue
            elif i_array[0] < 0:
                negative_num_count += len(i_array)
                continue
            left = 0
            right = len(i_array)-1
            while left < right:
                mid = left+(right-left)//2
                if i_array[mid] < 0:
                    right = mid
                elif i_array[mid] >= 0:
                    left = mid+1
            negative_num_count += len(i_array)-right
        return negative_num_count
        