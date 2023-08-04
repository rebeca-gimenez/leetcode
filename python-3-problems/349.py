# -*- coding: utf-8 -*-
"""
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of 
their intersection. Each element in the result must be unique 
and you may return the result in any order.
"""
def intersection(nums1, nums2):
    intersec = set()
    for num in nums1:
        for num2 in nums2:
            if num == num2:
                intersec.add(num)
    return list(intersec)

def intersection2(nums1, nums2):
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    nums1.sort()
    nums2.sort()
    intersec = set()
    for num in nums1:
        if num in nums2:
            intersec.add(num)
    return list(intersec)
nums1 = [1,2,2,1]
nums2 = [2,2]
output = [2]
print(intersection2(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
output = [9,4]
print(intersection2(nums1, nums2))
