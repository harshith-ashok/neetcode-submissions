class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        l, r = height[l], height[r]
        res = 0
        while l < r:
            if l < r:
                l += 1
                l = max(l, height[l])
                res += l - height[l]
            else:
                r -= 1
                r = max(r, height[r])
                res += r - height[r]
        return res