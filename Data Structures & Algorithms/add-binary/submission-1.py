class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a+b,2))[2:]