class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ['()','[]','{}']
        s = [i for i in s]
        if len(s) == 2:
            if "".join(s) in brackets:
                return True
            else:
                return False
        for i in s:
            for j in s:
                if i+j in brackets:
                    s.remove(i)
                    s.remove(j)
        s = "".join(s)
        print(s)
        if s in brackets:
            return True
        else:
            return False