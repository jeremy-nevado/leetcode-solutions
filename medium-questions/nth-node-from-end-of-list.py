class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        curr, prev, tail = head, None, head
        for i in range(n):
            tail = tail.next

        while tail:
            prev, curr, tail = curr, curr.next, tail.next
        if not prev:
            return head.next

        prev.next = curr.next
        return head
