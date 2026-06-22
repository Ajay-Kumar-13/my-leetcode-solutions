class MinStack(object):

    def __init__(self):
        self.stack = []
        self.topEle = -1
        self.auxiliary_stack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if len(self.auxiliary_stack) == 0:
            self.auxiliary_stack.append(value)
        else:
            top = self.auxiliary_stack[self.topEle]
            if value > top:
                self.auxiliary_stack.append(top)
            else:
                self.auxiliary_stack.append(value)
        self.topEle += 1

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.auxiliary_stack.pop()
        self.topEle -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.topEle]

    def getMin(self):
        """
        :rtype: int
        """
        return self.auxiliary_stack[self.topEle]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()