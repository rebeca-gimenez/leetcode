'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.
'''
def isAnagram2(s, t):
    if len(s) != len(t):
            return False
    else:
        for letter in s:
            if letter in t:
                t = t.replace(letter,'',1)
            else:
                return False
        return True
#Another solution with better time but worse memory
def isAnagram(s, t):
    if len(s) != len(t):
            return False
    else:
        s_dict = dict()
        t_dict = dict()
        for index in range(len(s)):
            if s[index] in s_dict:
                s_dict[s[index]] += 1
            else:
                s_dict[s[index]] = 1
            if t[index] in t_dict:
                t_dict[t[index]] += 1
            else:
                t_dict[t[index]] = 1
        
        return s_dict==t_dict
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
#output == True

s = "rat"
t = "car"
print(isAnagram(s, t))
#output == False