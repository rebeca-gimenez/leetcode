# -*- coding: utf-8 -*-
"""
1021. Remove Outermost Parentheses

A valid parentheses string is either empty "", "(" + A + ")", or A + B, 
where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, 
and there does not exist a way to split it into s = A + B, with A and B nonempty
 valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: 
    s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in 
the primitive decomposition of s.

Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
"""
def removeOuterParentheses2(s):
    primitive = ''
    stack = ''
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        stack += char
        #print(char, stack, count)
        if count == 0:
            try:
                primitive += stack[1:len(stack)-1]
            except:
                pass
            stack = ''
    return primitive
def removeOuterParentheses(s):
    primitive = ''
    stack = ''
    start = 1
    for num in range(len(s)):
        char = s[num]
        #print('stack', stack)
        if char == '(':
            stack += char
        else:
            stack = stack[:-1]
        if len(stack) == 0:
            #We found one primitive!
            primitive += s[start:num]
            start = num + 2
    return primitive
s = '(()(()))'
output = '()(())'
print(removeOuterParentheses(s) == output)
# (()(
# (())
s = '((()))'
output = "(())"
print(removeOuterParentheses(s)==output)
s = "(()())(())"
output = "()()()"
print(removeOuterParentheses(s)==output)
s = "(()())(())(()(()))"
output = "()()()()(())"
print(removeOuterParentheses(s)==output)
s = "()()"
output = ""
print(removeOuterParentheses(s)==output)