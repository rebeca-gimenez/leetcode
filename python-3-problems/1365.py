'''
1365. How Many Numbers Are Smaller Than the Current Number
Given the array: nums.
For each nums[i] find out how many numbers in the array are smaller than it. 
For each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
'''

def smallerNumbersThanCurrent(nums):
    answer = []
    for number in nums:
        copy = list(nums)
        copy.remove(number)
        if max(copy) < number:
            answer.append(len(copy))
        else:
            count = 0
            for element in copy:
                if element < number:
                    count = count + 1
            answer.append(count)
    return answer

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))    
