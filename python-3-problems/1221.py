'''
1221. Split a String in Balanced Strings
Balanced strings are those that have an equal quantity of 'L' and 'R' 
characters.

Given a balanced string s, split it into some number of substrings 
such that each substring is balanced.
Return the maximum number of balanced strings you can obtain.
'''
def balancedStringSplit(s):
    answer = 0
    answer1 = str()
    for letter in s:
        answer1 = answer1 + letter
        if answer1.count("R") == answer1.count("L"):
            answer = answer + 1
            answer1 = str()
    return answer
s = "RLRRLLRLRL"
print(balancedStringSplit(s))
s = "RLRRRLLRLL"
print(balancedStringSplit(s))
s = "LLLLRRRR"
print(balancedStringSplit(s))
        
            