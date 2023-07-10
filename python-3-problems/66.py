'''
66. Plus One
You are given a large integer represented as an integer array 
digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not
 contain any leading 0's.

Increment the large integer by one and return the resulting 
array of digits.

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''
def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        number = 0
        lenght = len(digits)
        for index in range(lenght):
            number += digits[index]*10**(lenght - index - 1)
        number = str(number + 1)
        answer = []
        for letter in number:
            answer.append(int(letter)) 
        return answer

digits = [1,2,3]
output = [1,2,4]
print(plusOne(digits), output)

digits = [9,9,9]
output = [1,0,0,0]
print(plusOne(digits), output)

digits = [4,3,2,1]
output = [4,3,2,2]
print(plusOne(digits), output)


digits = [9]
output = [1,0]
print(plusOne(digits), output)