"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
Follow up: Could you solve it without reversing the input lists?
"""
from typing import List, Optional
# from leetcode.src.add_two_numbers import add_two_numbers


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


def add_two_numbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Function creating new linked list with reversed values
    def reverse(node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        values.reverse()
        head = current = None
        for value in values:
            if current:
                current.next = ListNode(value)
                current = current.next
            else:
                head = current = ListNode(value)
        return head

    # Reversing two input lists
    r1 = reverse(l1)
    r2 = reverse(l2)
    # Adding two lists
    head = current = None
    remainder = 0
    while r1 or r2 or remainder:
        val1 = val2 = 0
        if r1:
            val1 = r1.val
            r1 = r1.next
        if r2:
            val2 = r2.val
            r2 = r2.next
        val = (val1 + val2 + remainder) % 10
        remainder = (val1 + val2 + remainder) // 10
        if current:
            current.next = ListNode(val)
            current = current.next
        else:
            head = current = ListNode(val)
    # Reversing the result
    return reverse(head)


def add_two_numbers2_2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 and not l2:
        return None
    l1_num = 0
    while l1:
        l1_num = l1_num * 10 + l1.val
        l1 = l1.next
    l2_num = 0
    while l2:
        l2_num = l2_num * 10 + l2.val
        l2 = l2.next
    lsum = l1_num + l2_num
    head = cur = ListNode()
    for istr in str(lsum):
        cur.next = ListNode(int(istr))
        cur = cur.next
    return head.next


p1 = LinkedList([7,2,4,3])
p2 = LinkedList([5,6,4])
print(add_two_numbers2(p1.head, p2.head))
print(add_two_numbers2_2(p1.head, p2.head))

p1 = LinkedList([0])
p2 = LinkedList([0])
print(add_two_numbers2(p1.head, p2.head))
print(add_two_numbers2_2(p1.head, p2.head))

p1 = LinkedList([2,4,3])
p2 = LinkedList([5,6,4])
print(add_two_numbers2(p1.head, p2.head))
print(add_two_numbers2_2(p1.head, p2.head))
