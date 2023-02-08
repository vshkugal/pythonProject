"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Constraints:
    k == lists.length
    0 <= k <= 10**4
    0 <= lists[i].length <= 500
    -10**4 <= lists[i][j] <= 10**4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10**4.
"""
from typing import List, Optional
import heapq


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


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    k = len(lists)
    available_indexes = set(n for n in range(k))
    for i in range(k):
        if not lists[i]:
            available_indexes.remove(i)
    head = current = ListNode()
    while len(available_indexes) > 0:
        min_val = min(lists[i].val for i in available_indexes)
        for i in available_indexes:
            if lists[i].val == min_val:
                current.next = lists[i]
                current = current.next
                lists[i] = lists[i].next
                if not lists[i]:
                    available_indexes.remove(i)
                break
    return head.next


def merge_k_lists1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    values, head, pointer = [], None, None
    for l in lists:
        while l:
            heapq.heappush(values, l.val)
            l = l.next
    while values:
        if head is None:
            head = ListNode(heapq.heappop(values))
            pointer = head
        else:
            pointer.next = ListNode(heapq.heappop(values))
            pointer = pointer.next
    return head


def merge_k_lists2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    # initialize heap
    heap = [(node.val, i) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    # initialize nodelist to return
    head = ListNode()
    node = head
    # merge
    while heap:
        # pop the min from heap
        value, i = heapq.heappop(heap)
        # add node to output chain
        node.next = ListNode(value)
        node = node.next
        # move the pointer to the next node if there is one
        if lists[i].next:
            lists[i] = lists[i].next
            new_value = lists[i].val
            # push next element into the heap
            heapq.heappush(heap, (new_value, i))
    return head.next


p1 = ListNode(1, ListNode(4, ListNode(5)))
p2 = ListNode(1, ListNode(3, ListNode(4)))
p3 = ListNode(2, ListNode(6))

print(merge_k_lists([p1, p2, p3]))
