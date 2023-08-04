# -*- coding: utf-8 -*-
"""
1859. Sorting the Sentence
A sentence is a list of words that are separated by a single space with no 
leading or trailing spaces. 
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word 
then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as 
"sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, 
reconstruct and return the original sentence.

2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.
"""
def sortSentence(s):
    words = s.split()
    answer = {}
    for word in words:
        answer[int(word[-1])]=word[:len(word)-1]
    answer2 = ""
    for idx in range(len(words)):
        answer2 += answer[idx+1] + " "
    return answer2[:len(answer2)-1]

s = "is2 sentence4 This1 a3"
output = "This is a sentence"
print(sortSentence(s))
s = "Myself2 Me1 I4 and3"
output = "Me Myself and I"