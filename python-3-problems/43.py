'''
43. Multiply Strings
Given two non-negative integers num1 and num2 
represented as strings, return the product of num1 and num2, 
also represented as a string.

Note: You must not use any built-in BigInteger library or 
convert the inputs to integer directly.

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, 
except the number 0 itself.
'''
def multiply(num1, num2):
    nums_dic = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    multiply = 0
    if len(num1) >= len(num2):
        max_num = num1
        min_num = num2
    else:
        max_num = num2
        min_num = num1
    count = 0
    for min_idx in range(len(min_num) - 1, -1, -1):
        place = 10**count
        for max_idx in range(len(max_num) - 1, -1, -1):
            #print(min_num[min_idx] + "*" + max_num[max_idx] + "*" + str(place) + "=", nums_dic[max_num[max_idx]]*nums_dic[min_num[min_idx]]*place)
            multiply += nums_dic[max_num[max_idx]]*nums_dic[min_num[min_idx]]*place
            place *= 10
        count += 1
    return str(multiply)
        
        
num1 = "2"
num2 = "3"
output = "6"
#print(multiply(num1, num2) == output)
num1 = "123"
num2 = "45"
print(multiply(num1, num2))
num1 = "123"
num2 = "456"
output = "56088"
print(multiply(num1, num2) == output)
        
        
 