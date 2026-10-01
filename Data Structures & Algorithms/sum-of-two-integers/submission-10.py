from math import log2
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFF
        MAX_INT = 0x7FFFF

        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = carry

        return a if a <= MAX_INT else ~(a ^ MASK)