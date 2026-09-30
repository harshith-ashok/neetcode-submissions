class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for i in s:
            if i in mp:
                mp[i]+=1
            else:
                mp[i] = 1
        for j in range(len(s)):
            if mp[s[j]] == 1:
                return j
        else:
            return -1