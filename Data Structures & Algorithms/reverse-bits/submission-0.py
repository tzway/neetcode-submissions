class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert to binary and pad with zeros
        binary_string = f"{n:0{32}b}"
        return int(binary_string[::-1], 2)
