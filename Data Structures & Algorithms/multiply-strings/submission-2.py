class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        prod = 0
        for i, digit1 in enumerate(num1[::-1]):
            for j, digit2 in enumerate(num2[::-1]):
                prod += int(digit1) * int(digit2) * 10 ** (i + j)
        
        return str(prod)

