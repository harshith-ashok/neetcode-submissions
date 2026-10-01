class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(int(a,2)+int(b,2),2))[2:]