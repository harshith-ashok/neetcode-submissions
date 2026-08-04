from itertools import count

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        return max((sum(x+i in s for i in count()) for x in s if x-1 not in s), default=0)