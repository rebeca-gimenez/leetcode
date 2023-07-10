'''
2089. Find Target Indices After Sorting Array
You are given a 0-indexed integer array nums and a target 
element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting 
nums in non-decreasing order. If there are no target indices, 
return an empty list. The returned list must be sorted in 
increasing order.

1 <= nums.length <= 100
1 <= nums[i], target <= 100
'''
def targetIndices(nums, target):    
    output = []
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = int((right + left)/2)
        #print(left, middle, right, nums, nums[left], nums[middle], nums[right])
        if nums[middle] == target:
            #Check if there is target to the left
            while middle >= 0 and nums[middle] == target:
                output.append(middle)
                middle -= 1
            #Check if there is target to the right
            middle = int((right + left)/2) + 1
            while middle <= len(nums) - 1 and nums[middle] == target:
                output.append(middle)
                middle += 1 
            break
        elif nums[middle] < target: 
            left = middle + 1
        else:
            right = middle - 1
    output.sort()
    return output

nums = [1,2,5,2,3]
target = 2
output = [1,2]
print(targetIndices(nums, target))
nums = [1,2,5,2,3]
target = 3
output = [3]
print(targetIndices(nums, target))
nums = [1,2,5,2,3]
target = 5
output = [4]
print(targetIndices(nums, target))