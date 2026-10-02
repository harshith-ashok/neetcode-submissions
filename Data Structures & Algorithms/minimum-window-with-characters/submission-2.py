from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        l = 0
        res = ""

        for r, c in enumerate(s):
            have[c] += 1

            while all(have[x] >= need[x] for x in need):
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]
                have[s[l]] -= 1
                l += 1

        return res