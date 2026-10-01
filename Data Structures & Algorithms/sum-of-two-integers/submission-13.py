from math import log2
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        while b!=0:
            carry = a&b
            a ^= b
            b = carry << 1
        return a
