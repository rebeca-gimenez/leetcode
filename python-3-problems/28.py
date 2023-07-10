'''
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index
 of the first occurrence of needle in haystack, or -1 if 
 needle is not part of haystack.
'''
def strSt2(haystack, needle):
    top = len(haystack)
    bottom = len(needle)
    for index in range(top):
        if index + bottom <= top:
            if haystack[index:index + bottom] == needle:
                return index
        else:
            return -1
#strSt2 had runtime error

def strStr(haystack, needle):
    if needle in haystack:
        for index in range(len(haystack)):
            if haystack[index] == needle[0]:
                if haystack[index:index + len(needle)] == needle:
                    return index
    else:
        return -1
    
#Tests
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle), 'Output: 0')
haystack = "sadbutsad"
needle = "but"
print(strStr(haystack, needle), 'Output: 3')
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle), 'Output: -1')
haystack = "hello"
needle = "ll"
print(strStr(haystack, needle), 'Output: 2')
haystack = "a"
needle = "a"
print(strStr(haystack, needle),'Output: 0')
haystack = "abc"
needle = "c"
print(strStr(haystack, needle),'Output: 2')