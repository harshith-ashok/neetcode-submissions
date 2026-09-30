class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x=1
        for i in nums:
            if i > 0 and x == i:
                print(x)
                x+=1
        return x