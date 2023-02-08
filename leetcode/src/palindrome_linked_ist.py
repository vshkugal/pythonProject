"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
    The number of nodes in the list is in the range [1, 10**5].
    0 <= Node.val <= 9
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list with values based on List values.
class LinkedList:
    def __init__(self, values: List):
        self.head = current = None
        for value in values:
            if current:
                current.next = ListNode(value)
                current = current.next
            else:
                self.head = current = ListNode(value)

    def __str__(self):
        node = self.head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return str(values)

    # Function finding the middle ListNode in the LinkedList
    def find_middle_node(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Function reversing the original LinkedList
    def reverse(self):
        node = self.head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node
        self.head = prev
        return self

    # Function creating new LinkedList with reversed values
    def reversed(self):
        node = self.head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        values.reverse()
        return LinkedList(values)

    # Function checking if LinkedList is a palindrome without altering the original LinkedList
    def is_palindrome(self) -> bool:
        forward = self.head
        backward = self.reversed().head
        middle = self.find_middle_node()
        while forward != middle:
            # print(forward.val)
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.next
        return True

    # Function checking if LinkedList is a palindrome and corrupting the original LinkedList in the process
    def is_palindrome1(self) -> bool:
        fast = slow = head = self.head
        # find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

    # Function checking if LinkedList is a palindrome and corrupting the original LinkedList in the process
    def is_palindrome2(self) -> bool:
        fast = slow = head = self.head
        prev = None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


# -----------------------------------------------------------------
# My external function checking whether linked list is a palindrome
# -----------------------------------------------------------------
def is_palindrome(head: Optional[ListNode]) -> bool:
    my_list = []
    while head:
        my_list.append(head.val)
        head = head.next
    l = len(my_list)
    for i in range(int(l/2)):
        if my_list[i] != my_list[l-i-1]:
            return False
    return True


# Another external function checking whether linked list is a palindrome
# and corrupting the original LinkedList in the process
def is_palindrome1(head: Optional[ListNode]) -> bool:
    def reverse(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev, node = node, next_node
        return prev
    # find the middle node
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # compare the first and second half nodes
    n1 = head
    n2 = reverse(slow.next)
    while n2:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next
    return True


# My external function finding the middle node of the linked list
def find_middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


p1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
p2 = ListNode(1, ListNode(2))
p3 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(is_palindrome(p1))
print(is_palindrome(p2))
print(is_palindrome(p3))
print(find_middle_node(p3).val)

p1 = LinkedList([1, 2, 2, 1])
p2 = LinkedList([1, 2])
p3 = LinkedList([1, 2, 3, 2, 1])
p4 = LinkedList([1, 2, 2, 2, 2, 1])
p5 = LinkedList([1, 2, 2, 2, 2, 2, 1])
print(is_palindrome(p1.head))
print(is_palindrome(p2.head))
print(is_palindrome(p3.head))
print(is_palindrome(p4.head))
print(is_palindrome(p5.head))
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

print("\nClass function is_palindrome()")
print(p1.is_palindrome())
print(p2.is_palindrome())
print(p3.is_palindrome())
print(p4.is_palindrome())
print(p5.is_palindrome())
print(p3.find_middle_node().val)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

print("\nClass function is_palindrome1()")
print(p1.is_palindrome1())
print(p2.is_palindrome1())
print(p3.is_palindrome1())
print(p4.is_palindrome1())
print(p5.is_palindrome1())
print(p3.find_middle_node().val)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

print("\nClass function is_palindrome2()")
p1 = LinkedList([1, 2, 2, 1])
p2 = LinkedList([1, 2])
p3 = LinkedList([1, 2, 3, 2, 1])
p4 = LinkedList([1, 2, 2, 2, 2, 1])
p5 = LinkedList([1, 2, 2, 2, 2, 2, 1])
print(p1.is_palindrome2())
print(p2.is_palindrome2())
print(p3.is_palindrome2())
print(p4.is_palindrome2())
print(p5.is_palindrome2())
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
