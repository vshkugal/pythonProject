"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the n-th node from the end of the list and return its head.
Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
Follow up: Could you do this in one pass?
"""
from typing import Optional


# Definition for singly-linked list.
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


def remove_n_th_node_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = head
    for _ in range(n-1):
        fast = fast.next
    prev = None
    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next
    if slow == head:
        return slow.next
    if not prev:
        return prev
    prev.next = slow.next
    return head


def remove_n_th_node_from_end1(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    for i in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def remove_n_th_node_from_end2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = head
    for i in range(n):
        fast = fast.next
        if fast is None:
            head = head.next
            return head
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


p1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
p2 = ListNode(1)
p3 = ListNode(1, ListNode(2))
p4 = ListNode(1, ListNode(2))

print(remove_n_th_node_from_end(p1, 2))
print(remove_n_th_node_from_end(p2, 1))
print(remove_n_th_node_from_end(p3, 1))
print(remove_n_th_node_from_end(p4, 2))
