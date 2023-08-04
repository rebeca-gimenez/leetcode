# -*- coding: utf-8 -*-
"""
1913. Maximum Product Difference Between Two Pairs
The product difference between two pairs (a, b) and (c, d) 
is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) 
is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, 
y, and z such that the product difference between pairs 
(nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
4 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""
def maxProductDifference(nums):
    nums.sort()
    return nums[-1]*nums[-2] - nums[0]*nums[1]
    
nums = [5,6,2,7,4]
output = 34
print(maxProductDifference(nums))

nums = [4,2,5,9,7,4,8]
output = 64
print(maxProductDifference(nums))