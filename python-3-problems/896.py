'''
896. Monotonic Array
An array is monotonic if it is either monotone increasing 
or monotone decreasing.

An array nums is monotone increasing if for all i <= j, 
nums[i] <= nums[j]. An array nums is monotone decreasing 
if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array
is monotonic, or false otherwise.

 1 <= nums.length <= 105
-105 <= nums[i] <= 105
'''
def isMonotonic(nums):
    count_inc = 0
    count_dec = 0
    for index in range(len(nums)-1):
        if nums[index+1]-nums[index] > 0:
            count_inc += 1
        elif nums[index+1]-nums[index] < 0:
            count_dec += 1
    if count_inc > 0 and count_dec == 0:
        return True
    elif count_dec > 0 and count_inc == 0:
        return True
    elif count_inc == 0 and count_dec == 0:
        return True
    else:
        return False
    
nums = [3]
output = True
print(isMonotonic(nums), output)

nums = [2,2]
output = True
print(isMonotonic(nums), output)

nums = [1,2,2,3]
output = True
print(isMonotonic(nums), output)

nums = [6,5,4,4]
output = True
print(isMonotonic(nums), output)

nums = [1,3,2]
output = False
print(isMonotonic(nums), output)