class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        print(nums)
        for i in range(len(nums)):
            if i == 0 and nums[i]-0 != 1:
                return 1
            elif i == len(nums):
                return nums[i]+1
            else:
                if nums[i]-nums[i+1] != 1:
                    return nums[i+1]