class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curProd = 1
        maxProd = nums[0]

        for i in nums:
            if curProd < 0:
                curProd=0
            curProd*=i
            maxProd = max(maxProd, curProd)
        
        return maxProd