class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=[i for i in s if i.isalpha()]
        return s == s[::-1]