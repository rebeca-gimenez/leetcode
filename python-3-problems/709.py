'''
709. To Lower Case
Given a string s, 
return the string after replacing every uppercase letter 
with the same lowercase letter.

1 <= s.length <= 100
s consists of printable ASCII characters.
'''
def toLowerCase(s):
    upper_dic ={'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    new = ''
    for index in range(len(s)):
        if s[index] in upper_dic:
            new = new + upper_dic[s[index]]
        else:
            new = new + s[index]     
    return new

s = "Hello"
print(toLowerCase(s))

s = "here"
print(toLowerCase(s))

s = "LOVELY"
print(toLowerCase(s))