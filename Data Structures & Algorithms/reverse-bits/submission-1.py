class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:].zfill(32)
        s = s[::-1]
        return int(s, 2)