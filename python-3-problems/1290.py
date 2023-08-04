# -*- coding: utf-8 -*-
"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of 
each node in the linked list is either 0 or 1. The linked list holds the 
binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

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

def list_to_linked(list1):
    if list1 == []:
        return ListNode(None)
    list1.reverse()
    next_node = None
    for item in list1:
        node = ListNode(item, next_node)
        next_node = node
    return node

def getDecimalValue2(head):
    #(1,(0,(1,None)))
    reverse = ListNode()
    next_node = None
    while head:
        reverse = ListNode(head.val,next_node)
        head = head.next
        next_node = reverse
    print(reverse)
    exp = 0
    num = 0
    while reverse.next is not None:
        num += reverse.val*2**exp
        reverse = reverse.next
        exp += 1
    num += reverse.val*2**exp
    head = ListNode(num)
    return head.val
def getDecimalValue(head):
    prev_head = 0
    while head.next is not None:
        head.val = prev_head*2 + head.val
        prev_head = head.val
        head = head.next
    head.val = prev_head*2 + head.val
    return head.val
head = [1,0,1]
output = 5
print(getDecimalValue(list_to_linked(head)))
head = [0]
output =  0
print(getDecimalValue(list_to_linked(head)))
head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
print(getDecimalValue(list_to_linked(head)))


