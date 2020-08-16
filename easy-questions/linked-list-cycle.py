class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle(self, head):
        passed_heads = [head]
        while head != None:
            if head.next in passed_heads:
                return True
            else:
                passed_heads.append(head.next)
                head = head.next
        return False

sol = Solution()
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(sol.hasCycle(node1))

node5 = ListNode(1)
node6 = ListNode(2)
node7 = ListNode(3)
node5.next = node6
node6.next = node7
print(sol.hasCycle(node5))

