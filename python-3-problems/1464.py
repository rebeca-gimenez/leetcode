# -*- coding: utf-8 -*-
"""
1464. Maximum Product of Two Elements in an Array
Given the array of integers nums, you will choose two different 
indices i and j of that array. Return the maximum value of 
(nums[i]-1)*(nums[j]-1).
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""
def maxProduct(nums):
    nums.sort()
    return (nums[-1]-1)*(nums[-2]-1)

nums = [3,4,5,2]
output = 12
print(maxProduct(nums))
nums = [1,5,4,5]
output = 16
print(maxProduct(nums))
nums = [3,7]
output = 12
print(maxProduct(nums))
