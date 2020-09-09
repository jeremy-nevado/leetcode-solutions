class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# TODO finish implementing min stack

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = self.tail = Node()
        

    def push(self, x: int) -> None:
        if self.head == None:
            self.head.val = x
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next()


    def pop(self) -> None:
        
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
