"""
2160. Minimum Sum of Four Digit Number After Splitting Digits
You are given a positive integer num consisting of exactly four digits. 
Split num into two new integers new1 and new2 by using the digits found in num. 
Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: 
    two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are 
    [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
1000 <= num <= 9999
"""
def minimumSum(num):
    num = str(num)
    numbers = []
    for letter in num:
        numbers.append(int(letter))
    numbers.sort()
    num1 = int(str(numbers[0]) + str(numbers[3]))
    num2 = int(str(numbers[1]) + str(numbers[2]))
    return num1 + num2
    
num = 2932
output = 52
print(minimumSum(num), output)
num = 4009
output = 13
print(minimumSum(num), output)
num = 1234
output = 37
print(minimumSum(num), output)