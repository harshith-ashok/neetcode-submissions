class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            if n not in seen:
                seen[n] = 0
            if n in seen:
                seen[n] += 1
        
        
        return list(j for j, v in seen.items() if v >= k)