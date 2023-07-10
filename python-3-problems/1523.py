'''
1523. Count Odd Numbers in an Interval Range
Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).
0 <= low <= high <= 10^9
'''
def countOdds(low, high):
    #If high is odd, we make it even
    if high % 2 != 0:
        high += 1
    #If low is odd, we make it even    
    if low % 2 != 0:
        low -= 1
    return (high - low) /2
        
print(4 // 2)
low = 3
high = 7
output = 3
print(countOdds(low, high)==output)
low = 8
high = 10
output = 1
print(countOdds(low, high)==output)