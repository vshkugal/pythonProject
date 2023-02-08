"""
Имеется linked list структуры, в котором хранятся числовые значения.
Реализовать функцию для суммирования 2-ух linked list. Длина листов может быть различна.
Пример: даны L1: [1, 2, 3], L2: [9,12, 24] и на выходе получается [10,14,27].
(для решения данной задачи нужно реализовать классы, описывающие работу с linked list структурой).
"""
from typing import List, Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class LinkedList:
    def __init__(self, values=[]):
        self.head = current = None
        for value in values:
            if current:
                current.next = ListNode(value)
                current = current.next
            else:
                self.head = current = ListNode(value)

    def __add__(self, other):
        head = current = None
        # values = []
        a1 = self.head
        a2 = other.head
        while a1 or a2:
            val1 = val2 = 0
            if a1:
                val1 = a1.val
                a1 = a1.next
            if a2:
                val2 = a2.val
                a2 = a2.next
            # values.append(val1 + val2)
        # return LinkedList(values)
            val = val1 + val2
            if current:
                current.next = ListNode(val)
                current = current.next
            else:
                head = current = ListNode(val)
        result_list = LinkedList()
        result_list.head = head
        return result_list

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def __str__(self):
        node = self.head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return str(values)

    def find_middle_node(self) -> Optional[ListNode]:
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


L1 = LinkedList([1, 2, 3])
L2 = LinkedList([9, 12, 24])
print(L1+L2)

p1 = LinkedList([1, 2, 2, 1])
p2 = LinkedList([1, 2])
p3 = LinkedList([1, 2, 3, 2, 1])

print(p1+p2)
print(p1+p2+p3)
print(len(p1+p2+p3))

print("\nClass function reverse() - reversing the original LinkedList")
p4 = p1+p2+p3
print(p4)
print(p4.reverse())
print(p4)

print("\nClass function reversed() - creating new LinkedList with reversed values")
p4 = p1+p2+p3
print(p4)
print(p4.reversed())
print(p4)
