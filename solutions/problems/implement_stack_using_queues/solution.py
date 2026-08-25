class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.topEle = 0

    def push(self, x: int) -> None:
        
        self.q1.append(x)
        self.topEle = x

    def pop(self) -> int:
        val  = 0

        while len(self.q1) > 0:
            val = 0
            if len(self.q1) == 1:
                val = self.q1.pop(0)
            else:
                self.q2.append(self.q1.pop(0))

        while len(self.q2) > 0:
            if len(self.q2) == 1:
                self.topEle = self.q2[0]
            self.q1.append(self.q2.pop(0))

        return val

    def top(self) -> int:
        return self.topEle

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()