"""
67. Add Binary
Given two binary strings a and b, 
return their sum as a binary string.

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros 
except for the zero itself.
"""
def addBinary(a, b):
    num_a = 0
    num_b = 0
    for index in range(len(a)):
        num_a += int(a[index])*2**(len(a) - 1 - index)
    for index in range(len(b)):
        num_b += int(b[index])*2**(len(b) - 1 - index)
    return str(bin(num_a + num_b))[2:]
        
a = "11"
b = "1"
output = "100"
print(addBinary(a, b) == output)
a = "1010"
b = "1011"
output = "10101"
print(addBinary(a, b) == output)