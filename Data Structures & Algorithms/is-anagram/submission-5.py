class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = str(sorted(list(s)))
        t = str(sorted(list(t)))

        if s == t:
            return True
        else:
            return False