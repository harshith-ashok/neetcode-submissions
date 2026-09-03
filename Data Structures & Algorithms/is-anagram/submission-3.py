class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t[::-1]:
            return True
        else:
            return False