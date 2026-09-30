class Solution:
    def reverseBits(self, n: int) -> int:
        new = bin(n)[2:].zfill(32)
        return int(new[::-1],2)