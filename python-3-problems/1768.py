'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''

def mergeAlternately2(word1,word2):
    answer = ''
    maxlen = max(len(word1),len(word2))
    for index in range(maxlen):
        if (index+1) <= len(word1):
            answer = answer + word1[index]
        if (index+1) <= len(word2):
            answer = answer + word2[index]
    return answer
def mergeAlternately(word1,word2):
    answer = ''
    wordslen = [len(word1), len(word2)]
    if wordslen[0] > wordslen[1]:
        for index in range(wordslen[1]):
            answer = answer + word1[index] + word2[index]
        answer = answer + word1[wordslen[1]:wordslen[0]]
    elif wordslen[0] == wordslen[1]:
        for index in range(wordslen[1]):
            answer = answer + word1[index] + word2[index]
    else: 
        for index in range(wordslen[0]):
            answer = answer + word1[index] + word2[index]
        answer = answer + word2[wordslen[0]:wordslen[1]]
    return answer
#Testing
word1 = "abc"
word2 = "pqr"
computed = mergeAlternately(word1,word2)
expected = "apbqcr"
print(computed == expected)

word1 = "ab"
word2 = "pqrs"
computed = mergeAlternately(word1,word2)
expected = "apbqrs"
print(computed == expected)

word1 = "abcd"
word2 = "pq"
computed = mergeAlternately(word1,word2)
expected = "apbqcd"
print(computed == expected)