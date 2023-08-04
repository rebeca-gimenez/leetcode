"""
942. DI String Match
A permutation perm of n + 1 integers of all the integers in the range [0, n] 
can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. 
If there are multiple valid permutations perm, return any of them.

1 <= s.length <= 105
s[i] is either 'I' or 'D'
"""
def diStringMatch(s):
    nums = [num for num in range(len(s)+1)]
    perm = [0]*(len(s)+1)
    for index in range(len(s)):
        if s[index] == "I":
            perm[index] = nums[0]
            nums.pop(0)
        else:
            perm[index] = nums[-1]
            nums.pop(-1)
    perm[-1] = nums[0]
    return perm
            
s = "IDID"
output = [0,4,1,3,2]
print(diStringMatch(s)==output)
s = "III"
output = [0,1,2,3]
print(diStringMatch(s)==output)
s = "DDI"
output = [3,2,0,1]
print(diStringMatch(s)==output)