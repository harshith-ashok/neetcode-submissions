import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = re.sub(r'[^0-9a-zA-Z]', '', s)
        print(s)
        if s == s[::-1]:
            return True
        if len(s) <= 1:
            return True
        else:
            return False