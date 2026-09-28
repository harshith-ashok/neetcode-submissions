class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = []
        for num in nums:
            max_count.append(nums.count(num))

        return sorted(max_count)