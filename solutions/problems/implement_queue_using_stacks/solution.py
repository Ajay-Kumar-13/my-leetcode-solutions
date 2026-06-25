class MyQueue(object):

    def __init__(self):
        self.q = []
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push all the elements in s1 to s2
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
            
        # push x into s1
        self.s1.append(x)
        
        # bring back all the elements from s2
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.s1) == 0 and len(self.s2) == 0)
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()