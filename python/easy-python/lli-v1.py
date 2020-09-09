class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        passed_heads = []
        a = headA
        b = headB
        while a:
            passed_heads.append(a)
            a = a.next
        while b:
            if b in passed_heads:
                return b.val
            else:
                b = b.next
        return None

