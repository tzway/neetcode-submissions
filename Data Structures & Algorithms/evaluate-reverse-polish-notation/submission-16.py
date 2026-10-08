class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        for tk in tokens:
            if tk in operators:
                right = stack.pop()
                left = stack.pop()
                if tk == "+":
                    stack.append(right + left)
                elif tk == "-":
                    stack.append(left-right)
                elif tk == "*":
                    stack.append(left*right)
                elif tk == "/":
                    stack.append(
                        left//right if left*right >0 else -(-left//right)
                        )
            else:
                stack.append(int(tk))
        return stack[-1]