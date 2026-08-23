class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2  = []
        self.top = 0

    def push(self, x: int) -> None:
        if not self.s1:
            self.top = x

        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        val = self.s2.pop()

        while len(self.s2) > 0:
            x = self.s2.pop()
            if not self.s1:
                self.top = x
            self.s1.append(x)

        return val

    def peek(self) -> int:
        return self.top

    def empty(self) -> bool:
        if not self.s1:
            return True
        
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()