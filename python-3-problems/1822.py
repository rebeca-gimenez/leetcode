'''
1822. Sign of the Product of an Array
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. 
Let product be the product of all values in the array nums.

Return signFunc(product).

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
'''
def arraySign(nums):
    product = 1
    for number in nums:
        product = product*number
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0


nums = [-1,-2,-3,-4,3,2,1]
output = 1
print(arraySign(nums), output)

nums = [1,5,0,2,-3]
output = 0
print(arraySign(nums), output)

nums = [-1,1,-1,1,-1]
output = -1
print(arraySign(nums), output)