class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {
            ')': '(', '}': '{', ']': '['
            }

        for c in s:
            if c in closeOpen:
                if not stack:
                    return False
                if closeOpen[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack