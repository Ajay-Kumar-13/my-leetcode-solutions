class MyStack(object):

    def __init__(self):
        self.s = []
        self.q1 = []
        self.q2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        # push all the elements from q1 to q2
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))

        # add x to q1
        self.q1.append(x)

        # bring back all the elements from s2

        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))

        

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0 and len(self.q2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()