class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')','[':']','{':'}'}
        class Stack(list):
            def top(self):
                if self:
                    return self[-1]
            def push(self, c):
                self.append(c)
            def is_empty(self):
                return not self

        stack = Stack()
        for c in s:
            if c in pairs:
                stack.push(c)
                continue
            if c not in pairs:
                if not stack.is_empty() and pairs[stack.top()] == c:
                    stack.pop()
                    continue
                else:
                    return False
        
        return not bool(stack)
