class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = list(s)
        nums2 = list(t)

        for i in range(len(nums)):
            m = i

            for j in range(i + 1, len(nums)):
                if nums[j] < nums[m]:
                    m = j

            nums[i], nums[m] = nums[m], nums[i]

        for i in range(len(nums2)):
            m = i

            for j in range(i + 1, len(nums2)):
                if nums2[j] < nums2[m]:
                    m = j

            nums2[i], nums2[m] = nums2[m], nums2[i]

        return nums == nums2