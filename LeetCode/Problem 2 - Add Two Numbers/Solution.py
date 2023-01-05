from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = current = ListNode(-1)
        while l1 or l2 or carry:
            carry, sumval = divmod(
                sum(l and l.val or 0 for l in (l1, l2)) + carry, 10)
            current.next = current = ListNode(sumval)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return head.next
