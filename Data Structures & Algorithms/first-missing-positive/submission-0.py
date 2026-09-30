class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >=0:
                if nums[i]+1 not in nums:
                    return nums[i]+1

