'''
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of 
the array.

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    num_zeros = nums.count(0)
    if num_zeros > 0:
        while nums[(len(nums)-num_zeros):len(nums)] != [0]*num_zeros:
            nums.remove(0)
            nums.append(0)


nums = [0,0,1]
moveZeroes(nums)
print(nums)
output = [0,1,0]
print(nums+[0])


nums = [0,1,0,3,12]
#moveZeroes(nums)
#print(nums)
output = [1,3,12,0,0]
#print(output[3:5])
nums = [0]
output = [0]