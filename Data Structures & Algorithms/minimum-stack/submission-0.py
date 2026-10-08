class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return null

    def getMin(self) -> int:
        if not self.stack:
            return null
        m = self.top()
        for v in self.stack:
            m = min(m,v)
        return m
        
