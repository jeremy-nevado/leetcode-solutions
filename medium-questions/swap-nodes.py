class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or next.head == None:
            return head
        nxt, curr, prev = head.next, head, None
        head = head.next
        while nxt:
            if prev:
                prev.next = nxt
            curr.next = nxt.next
            nxt.next = curr
            prev = curr
            if curr.next:
                nxt = curr.next.next
            else:
                nxt = None
            curr = curr.next

        return head
