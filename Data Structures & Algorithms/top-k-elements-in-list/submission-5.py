class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for i,j in count.items():
            if i >= k:
                res.append(i)
        return res