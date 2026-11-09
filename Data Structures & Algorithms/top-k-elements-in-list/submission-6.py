class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
        
        sorted_nums = sorted(seen, key=seen.get, reverse=True)

        return sorted_nums[:k]