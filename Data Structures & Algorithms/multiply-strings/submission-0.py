class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == 0 or num2 == 0:
            return 0
        str_int = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }

        prod = 0
        for i, digit1 in enumerate(num1[::-1]):
            for j, digit2 in enumerate(num2[::-1]):
                prod += str_int[digit1] * str_int[digit2] * 10 ** (i + j)
        
        return str(prod)

