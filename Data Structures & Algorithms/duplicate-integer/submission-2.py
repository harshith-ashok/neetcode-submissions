class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in nums:
            if nums.count(i) > 1:
                return True
            else:
                 seen.append(i)
        return False