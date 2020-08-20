import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        return str(res)

class Solution:
    def isPalindrome(self, head):
        if not head:
            return True
        slow = head
        fast = head
        rev = None 
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
            
class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))))))
        self.assertTrue(Solution().isPalindrome(ListNode(1)))
        self.assertFalse(Solution().isPalindrome(ListNode(1, ListNode(2))))
if __name__ == '__main__':
    unittest.main()

