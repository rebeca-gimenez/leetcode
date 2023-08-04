# -*- coding: utf-8 -*-
"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
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

def middleNode(head):
    copy = head
    count = 0
    while head:
        head = head.next
        count += 1
    count = count//2
    while count > 0:
        copy = copy.next
        count -= 1
    return copy
    
head = [1,2,3,4,5]
output = [3,4,5]
print(middleNode(list_to_linked(head)))
head = [1,2,3,4,5,6]
output = [4,5,6]
print(middleNode(list_to_linked(head)))