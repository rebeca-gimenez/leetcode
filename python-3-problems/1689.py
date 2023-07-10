'''
Leetcode #1689
Partitioning Into Minimum Number Of Deci-Binary Numbers

A decimal number is called deci-binary if each of its digits 
is either 0 or 1 without any leading zeros. For example, 101
 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, 
return the minimum number of positive deci-binary numbers 
needed so that they sum up to n.
'''
#Since a deci-binary has either 0 or 1, the minimum number will be
#the maximum number of the string
#For example: 82 needs 10*8 to reach 80, so the minimum number is 8
#Either you reach 9 and stop (the max one digit number)
#Or you evaluate every number from the string
def decibinary(n): 
    return int(max(n))

print(decibinary("32"))
print(decibinary("82734"))
print(decibinary("27346209830709182346"))
        


