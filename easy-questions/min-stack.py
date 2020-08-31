class MinStack:

    def __init__(self):
        '''
        initialize your data structure here.
        '''
        self.stack = {"small": None, "top": None}

    def push(self, x):
        self.stack["top"] = x
        self.stack[x] = None
        if stack[small] > x:
            stack[small] = x;

    def pop(self):
        return None
        

    def top(self):
        return self.stack["top"]

    def getMin(self):
        return self.stack["small"]
