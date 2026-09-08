class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 0
        nums2 = nums.copy()
        nums_list = []
        
        for i in nums:
            nums2.remove(i)

            result = 1
            for j in nums2:
                result *= j
            nums_list.append(result)

            nums2 = nums.copy()

        return nums_list
