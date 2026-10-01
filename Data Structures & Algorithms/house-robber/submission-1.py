class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = 0
        if len(nums) <= 2:
            return max(nums)
        for i in range(0,len(nums),2):
            loot+=nums[i]
        return loot