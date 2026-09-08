class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_list = [1] * n

        prefix = 1
        for i in range(n):
            nums_list[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            nums_list[i] *= suffix
            suffix *= nums[i]

        return nums_list
