'''
1502. Can Make Arithmetic Progression From Sequence
A sequence of numbers is called an arithmetic progression 
if the difference between any two consecutive elements is 
the same.

Given an array of numbers arr, return true if the array 
can be rearranged to form an arithmetic progression. 
Otherwise, return false.

2 <= arr.length <= 1000
-106 <= arr[i] <= 106
'''
def canMakeArithmeticProgression(arr):
    if len(arr) < 2:
        return True
    else:
        arr.sort()
        dif = arr[1] - arr[0]
        for index in range(len(arr)-1):
            if arr[index] + dif != arr[index + 1]:
                return False
        return True 

def canMakeArithmeticProgression2(arr):
    if len(arr) < 2:
        return True
    else:
        arr.sort()
        dif = arr[1] - arr[0]
        test = []
        for index in range(len(arr)):
            test.append(arr[0] + dif*index)
        if test == arr:
            return True
        return False
    
arr = [1,2,3,2,5]
output = False
print(canMakeArithmeticProgression(arr), output)

arr = [3,5,1]
output = True
print(canMakeArithmeticProgression(arr), output)

arr = [1,2,4]
output = False
print(canMakeArithmeticProgression(arr), output)