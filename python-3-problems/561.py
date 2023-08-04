"""
561. Array Partition
Given an integer array nums of 2n integers, group these integers into n pairs 
(a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i 
is maximized. Return the maximized sum.
1 <= n <= 10^4
nums.length == 2 * n
-10^4 <= nums[i] <= 10^4
"""
def arrayPairSum(nums):
    pairs = 0
    nums.sort()
    while len(nums) > 0:
        pairs += min(nums[-1],nums[-2])
        nums.pop(-1)
        nums.pop(-1)
    return pairs
nums = [1,4,3,2]
output = 4
print(arrayPairSum(nums) == output)
nums = [6,2,6,5,1,2]
output =  9
print(arrayPairSum(nums) == output)