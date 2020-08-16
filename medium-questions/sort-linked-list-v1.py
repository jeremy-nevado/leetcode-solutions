# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        pnode = None
        nnode = None
        min_val = 0
        curr = head
        if head.next == None:
            return head
        while curr.next:
            if curr.val > curr.next.val:
                pnode = curr
                nnode = curr.next.next
                min_val = curr.next.val
            curr = curr.next
        if pnode == None:
            return ListNode(head.val, self.sortList(head.next))
        else:
            pnode.next = nnode
            return ListNode(min_val, self.sortList(head)) 

sol = Solution()
print(sol.sortList(ListNode(1, ListNode(0, ListNode(2, ListNode(3))))))
