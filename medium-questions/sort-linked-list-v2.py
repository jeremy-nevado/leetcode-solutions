class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy.next
        if not left:
            return right
        if not right:
            return left
        else:
            while left and right:
                if left.val < right.val:
                    curr = ListNode(left.val)
                    curr = curr.next
                    left = left.next
                else:
                    dummy.next = ListNode(right.val)
                    right = right.next
            if not left:
                curr = right
            elif not right:
                curr = left
        return dummy.next

sol = Solution()
print(sol.sortList(ListNode(1, ListNode(0, ListNode(3, ListNode(2))))))
