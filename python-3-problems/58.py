'''
58. Length of Last Word
Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring
consisting of non-space characters only.

 1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
def lengthOfLastWord2(s):
    s = s.strip()
    if s.count(' ') == 0:
        return len(s)
    index = -1
    #Find the index of the first letter of the word
    count = 0
    while s[index] != ' ' and abs(index) < len(s):
        count += 1
        index -= 1
    return count
        
def lengthOfLastWord(s):
    s_list = s.split()
    return len(s_list[-1])

s = "a        "
output = 1
print(lengthOfLastWord(s), output)    
            
s = "day"
output = 3
print(lengthOfLastWord(s), output)    

s = "Hello World"
output = 5
print(lengthOfLastWord(s), output)

s = "   fly me   to   the moon  "
output = 4
print(lengthOfLastWord(s), output)

s = "luffy is still joyboy"
output = 6
print(lengthOfLastWord(s), output)