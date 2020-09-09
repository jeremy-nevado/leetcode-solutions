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
        return res

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

class TestSolution(unittest.TestCase):
    def test_reverseList(self):
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2))).__repr__(), ListNode(2, ListNode(1)).__repr__())
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(21, ListNode(14)))))).__repr__(), ListNode(14, ListNode(21, ListNode(3, ListNode(2, ListNode(1))))).__repr__())

if __name__ == '__main__':
    unittest.main()

