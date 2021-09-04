"""
Problem Statement:
    Given an array of integers nums which is sorted in ascending order, and an integer target, 
    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.
Test Cases:
    [-1,0,3,5,9,12] and 9
    [-1,0,3,5,9,12] and 2
"""

# Approach 1: Iterative
# Time complexity: O(log n)
# Results: 
#   Runtime: 204 ms, faster than 49.63% of Python online submissions for Binary Search.
#   Memory Usage: 14.7 MB, less than 28.38% of Python online submissions for Binary Search.
class Solution(object):
    def search(self, nums, target):
        high_i = len(nums)-1
        low_i = 0
        while low_i <= high_i:
            mid_i = (high_i+low_i)//2
            if target == nums[mid_i]:
                return mid_i
            if nums[mid_i]>target:
                high_i = mid_i-1
            if nums[mid_i]<target:
                low_i = mid_i+1
        return -1

# Approach 2: Iterative 
# Bug with Approach 1 fix: https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
# Time complexity: O(log n)
# Results: 
#   Runtime: 192 ms, faster than 94.00% of Python online submissions for Binary Search.
#   Memory Usage: 14.6 MB, less than 55.29% of Python online submissions for Binary Search.
class Solution(object):
    def search(self, nums, target):
        high_i = len(nums)-1
        low_i = 0
        while low_i <= high_i:
            mid_i = low_i+((high_i-low_i)//2) # this line has changed
            if nums[mid_i] == target:
                return mid_i
            if nums[mid_i]>target:
                high_i = mid_i-1
            if nums[mid_i]<target:
                low_i = mid_i+1
        return -1