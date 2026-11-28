class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            for j in numbers:
                if i != j:
                    if i+j == target:
                        return [i,j]