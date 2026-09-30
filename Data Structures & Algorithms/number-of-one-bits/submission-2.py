class Solution:
    def hammingWeight(self, n: int) -> int:
        new = bin(n)[2:]
        nums = 0
        for i in new:
            if i == '1':
                nums+=1
        return nums
        