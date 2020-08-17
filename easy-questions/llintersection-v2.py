class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str([self.val])

class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while not a == b:
            a = headA if a == None else a.next
            b = headB if b == None else b.next
        return a
sol = Solution()

node1 = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))

node2 = ListNode(5, ListNode(6, ListNode(1, node1.next.next)))

print(sol.getIntersectionNode(node1, node2))

