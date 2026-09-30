from math import log

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return log(2**a * 2**b)