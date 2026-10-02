from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()
        l = 0
        count = 0
        res = ""

        for r, c in enumerate(s):
            have[c] += 1

            if c in need and have[c] == need[c]:
                count += 1

            while count == len(need):
                if not res or r - l + 1 < len(res):
                    res = s[l:r + 1]

                if s[l] in need and have[s[l]] == need[s[l]]:
                    count -= 1

                have[s[l]] -= 1
                l += 1

        return res