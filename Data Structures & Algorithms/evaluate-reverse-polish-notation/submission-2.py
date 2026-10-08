class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left+right)
            elif token == '-':
                stack.append(left-right)
            elif token == '*':
                stack.append(left*right)
            elif token == "/":
                # stack.append(left//right)
                if left*right >= 0:
                    sign = 1
                else:
                    sign = -1
                stack.append (abs(left)//abs(right)*sign)
        return stack.pop()