"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import List, Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return str(values)


# Definition for singly-linked list.
class LinkedList:
    def __init__(self, values: List):
        self.head = current = None
        for value in values:
            if current:
                current.next = ListNode(value)
                current = current.next
            else:
                self.head = current = ListNode(value)


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = current = None
    remainder = 0
    while l1 or l2 or remainder:
        val1 = val2 = 0
        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next
        val = (val1 + val2 + remainder) % 10
        remainder = (val1 + val2 + remainder) // 10
        if current:
            current.next = ListNode(val)
            current = current.next
        else:
            head = current = ListNode(val)
    return head


p1 = LinkedList([2,4,3])
p2 = LinkedList([5,6,4])
print(add_two_numbers(p1.head, p2.head))

p1 = LinkedList([0])
p2 = LinkedList([0])
print(add_two_numbers(p1.head, p2.head))

p1 = LinkedList([9,9,9,9,9,9,9])
p2 = LinkedList([9,9,9,9])
print(add_two_numbers(p1.head, p2.head))
