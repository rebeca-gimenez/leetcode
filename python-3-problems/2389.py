"""
2389. Longest Subsequence With Limited Sum
You are given an integer array nums of length n, 
and an integer array queries of length m.

Return an array answer of length m where answer[i] 
is the maximum size of a subsequence that you can 
take from nums such that the sum of its elements 
is less than or equal to queries[i].

A subsequence is an array that can be derived from 
another array by deleting some or no elements without 
changing the order of the remaining elements.

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""
def answerQueries(nums, queries):
    nums.sort()
    copy = list(queries)
    copy.sort()
    n = len(nums)
    m = len(queries)    
    answer = {}
    answer2 = []
    sums = 0
    idx_n = 0
    for idx_q in range(m):
        while idx_n <= n-1 and (sums + nums[idx_n]) <= copy[idx_q]:
            sums += nums[idx_n]
            idx_n += 1
        answer[copy[idx_q]] = idx_n
    for query in queries:
        answer2.append(answer[query])
    return answer2
nums = [1,2,4,5]
queries = [3,10,21]
output = [2,3,4]
print(answerQueries(nums, queries))
nums = [2,3,4,5]
queries = [1]
output = [0]
print(answerQueries(nums, queries))
nums = [736411,184882,914641,37925,214915]
queries = [331244,273144,118983,118252,305688,718089,665450]
output = [2,2,1,1,2,3,3]
print(answerQueries(nums, queries))