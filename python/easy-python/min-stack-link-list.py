class ListNode:
    def __init__(self, val=0, prev=None, currMin = None):
        self.val = val
        self.prev = prev 
        self.currMin = currMin

class MinStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        if not self.head:
            self.head = ListNode(x, None, x)
        else:
            if self.head.currMin > x:
                currMin = x
            else:
                currMin = self.head.currMin
            node = ListNode(x, self.head, currMin)
            self.head = node
        return None

    def top(self):
        return self.head.val

    def pop(self):
        self.head = self.head.prev
        return None

    def getMin(self):
        return self.head.currMin
        

