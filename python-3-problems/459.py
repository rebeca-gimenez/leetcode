'''
459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking 
a substring of it and appending multiple copies of the substring
together.
1 <= s.length <= 104
s consists of lowercase English letters
'''
def repeatedSubstringPattern(s):
    #First we search for the substring if it exists
    substring = ''
    for index in range(int(len(s)/2)):
        #Try only combinations that divide the len with module 0
        substring += s[index]
        if len(s) % (index + 1) == 0:
            copy = str(s)
           #copy = copy.replace(substring,'')
            if  copy.replace(substring,'') == '':
                return True
    return False
        
s = "abab"
print(repeatedSubstringPattern(s),True)
#Output: true

s = "aba"
print(repeatedSubstringPattern(s), False)
#Output: false

s = "abcabcabcabc"
print(repeatedSubstringPattern(s), True)
#Output: true

s = "abaababaab"
print(repeatedSubstringPattern(s), True)
#Output: true

s = "abacabacaba"
print(repeatedSubstringPattern(s), False)
