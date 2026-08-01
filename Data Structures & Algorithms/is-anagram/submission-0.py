class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = 0
        for i in s:
            if i in t:
                seen+=1
        if seen == len(t):
            return True
        else:
            return False
