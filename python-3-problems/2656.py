# -*- coding: utf-8 -*-
"""
2656. Maximum Sum With Exactly K Elements
You are given a 0-indexed integer array nums and an integer k. 
Your task is to perform the following operation exactly 
k times in order to maximize your score:

Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing 
the operation exactly k times.
1 <= nums.length <= 100
1 <= nums[i] <= 100
1 <= k <= 100
"""
def maximizeSum(nums, k):
    num = max(nums)
    answer = num
    k -= 1
    while k > 0:
        num += 1
        answer += num
        k -= 1
    return answer
nums = [1,2,3,4,5]
k = 3
output = 18
print(maximizeSum(nums, k) == output)
nums = [5,5,5]
k = 2
output = 11
print(maximizeSum(nums, k) == output)

