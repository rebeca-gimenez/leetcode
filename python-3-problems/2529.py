'''
2529. Maximum Count of Positive Integer and Negative Integer
Given an array nums sorted in non-decreasing order, 
return the maximum between the number of positive integers 
and the number of negative integers.

In other words, if the number of positive integers in nums 
is pos and the number of negative integers is neg, then return 
the maximum of pos and neg.
Note that 0 is neither positive nor negative.

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
 

Follow up: Can you solve the problem in O(log(n)) time complexity?
'''
def maximumCount(nums):
    def binarysearch(nums, pos, lef, rig):
        if lef > rig:
            return -1
        if pos:
            mid = int((lef + rig) / 2)
            if nums[mid] <= 0:
                return binarysearch(nums, pos, mid + 1, rig)
            else:
                return mid
        else:
            mid = int((lef + rig) / 2)
            if nums[mid] >= 0:
                return binarysearch(nums, pos, lef, mid - 1)
            else:
                return mid
    #Case 1: all numbers are positive
    if nums[0] > 0:
        return len(nums)
    #Case 2: all numbers are negative
    elif nums[len(nums) - 1] < 0:
        return len(nums)
    #Case 3
    else:
        #Binary search
        #Find the position were numbers turn from neg to pos
        #First find positive numbers
        pos = 0
        neg = 0
        idx_pos = binarysearch(nums, True, 0, len(nums) - 1)
        idx_neg = binarysearch(nums, False, 0, len(nums) - 1)
        #print("result pos", idx_pos, nums[idx_pos])
        #print("result neg", idx_neg, nums[idx_neg])
        #If we found a positive number
        if idx_pos > 0:
            while idx_pos >= 0 and nums[idx_pos] > 0:
                idx_pos -= 1
            pos = len(nums) - ( idx_pos + 1 )
            #print("pos", pos)
        if idx_neg >= 0:
            while idx_neg < len(nums) - 1 and nums[idx_neg] < 0:
                idx_neg += 1
            neg = idx_neg
            #print("neg", neg)
        return max(pos,neg)
            
            
nums = [-2,-1,-1,1,2,3]
output = 3
print(maximumCount(nums), maximumCount(nums) == output)
nums = [-3,-2,-1,0,0,1,2]
output = 3
print(maximumCount(nums), maximumCount(nums) == output)
nums = [5,20,66,1314]
output = 4
print(maximumCount(nums), maximumCount(nums) == output)
nums = [0,0,0]
output = 0
print(maximumCount(nums), maximumCount(nums) == output)
nums = [0,0,1]
output = 1
print(maximumCount(nums), maximumCount(nums) == output)
nums = [-2,-1,0,0,0]
output = 2
print(maximumCount(nums), maximumCount(nums) == output)