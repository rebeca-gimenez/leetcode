# -*- coding: utf-8 -*-
"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
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

def reverseList(head):
    nexnode = None
    if not head:
        return head
    else:
        while head:
            #(1,node(2, None))
            #head.val = 1
            #(2,(head.val, None))
            node = ListNode(head.val,nexnode)
            nexnode = node
            head = head.next
        return node


head = [1,2,3,4,5]
output = [5,4,3,2,1]
print(reverseList(list_to_linked(head)))
head = [1,2]
output = [2,1]
print(reverseList(list_to_linked(head)))
head = []
output = []
print(reverseList(list_to_linked(head)))