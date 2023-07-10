'''
976. Largest Perimeter Triangle
Given an integer array nums, 
return the largest perimeter of a triangle with a non-zero area, 
formed from three of these lengths. 
If it is impossible to form any triangle of a non-zero area, return 0.
3 <= nums.length <= 104
1 <= nums[i] <= 106
'''
def largestPerimeter(nums):
    nums.sort(reverse=True)
    print(nums)
    while len(nums) > 2:
        if nums[1] + nums[2] > nums[0]:
            return nums[1] + nums[2] + nums[0]
        nums.pop(0)            
    return 0
nums = [2,1,2]
#print(largestPerimeter(nums))
nums = [1,2,1,10]
#print(largestPerimeter(nums))
nums = [3,2,3,4]
print(largestPerimeter(nums))