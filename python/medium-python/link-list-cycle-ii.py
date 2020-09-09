# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        passed_heads = [head]
        while head != None:
            if head.next in passed_heads:
                return head.next
            else:
                passed_heads.append(head)
                head = head.next
        return "no cycle"
