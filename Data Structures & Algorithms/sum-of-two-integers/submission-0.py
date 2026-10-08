class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.add_bitwise_32bit(a,b)

    def add_bitwise_32bit(self, a, b):
        MASK = 0xFFFFFFFF  # Simulate 32-bit overflow
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            carry = a & b
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)
