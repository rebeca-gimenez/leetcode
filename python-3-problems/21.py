# -*- coding: utf-8 -*-
"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made 
by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        # .next is the next node (type: class ListNode)
        self.next = next 
    def __str__(self):
        answer = []
        while True:
            answer.append(self.val)
            if self.next == None:
                break
            self = self.next
        if answer == [None]:
            return str([])
        return str(answer)
    def __bool__(self):
        """Return bool(self)."""
        return self.val is not None
        
#Example
x = ListNode(1,ListNode(2))
#print('Example 1', x)

def list_to_linked(list1):
    if list1 == []:
        return ListNode(None)
    list1.reverse()
    next_node = None
    for item in list1:
        node = ListNode(item, next_node)
        next_node = node
    return node
#Example
x = [1,2,3]
#print('Example 2', list_to_linked(x))
x = []
#print('Example 3', list_to_linked(x))

#Leetcode solution.
def mergeTwoLists(list1, list2):
    #Create node: (0, None)
    answer = ListNode()
    node = answer
    while True:
        #Loop won't break until one of the lists is empty
        #Check if one of the lists is empty
        if not list1:
            #Replace node = (0, None) with node = (0, list2Node)
            node.next = list2
            break
        if not list2:
            #Replace node = (0, None) with node = (0, list1Node)
            node.next = list1
            break
        #If one is smaller, add that one
        if list1.val < list2.val:
            #Replace node = (0, None) with node = (0, list1Node)
            node.next = ListNode(list1.val)
            #Remove node from list
            #From (val1, next1) to (val2, next2) 
            #where next1 = (val2, next2) and next2 = (val3, next3)
            list1 = list1.next
        #Else, the other node is either equal or smaller, add the other node
        else:
            #Replace node = (0, None) with node = (0, list2Node)
            node.next = ListNode(list2.val)
            #Remove node from list
            #From (val1, next1) to (val2, next2) 
            #where next1 = (val2, next2) and next2 = (val3, next3)
            list2 = list2.next
        #We had node = (0, NewNode), change node = NewNode and repeat loop
        node = node.next
    return answer.next

list1 = [1,2,4]
list2 = [1,3,4]
output= [1,1,2,3,4,4]
print(mergeTwoLists(list_to_linked(list1), list_to_linked(list2)))
list1 = []
list2 = []
output= []
print(mergeTwoLists(list_to_linked(list1), list_to_linked(list2)))
list1 = []
list2 = [0]
output= [0]
print(mergeTwoLists(list_to_linked(list1), list_to_linked(list2)))