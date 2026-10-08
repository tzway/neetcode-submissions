from operator import add, sub, mul, floordiv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+":add, "-":sub, "*":mul, "/":lambda a,b: a//b if a*b>=0 else -(-a//b) }

        stack = []
        for tk in tokens:
            print(stack)
            if tk in operands:
                right = stack.pop()
                left = stack.pop()
                stack.append(operands[tk](left, right))

            else:
                stack.append(int(tk))

        return stack.pop()