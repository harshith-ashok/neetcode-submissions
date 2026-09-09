class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ['()','[]','{}']
        s = [i for i in s]
        for i in s:
            for j in s:
                print(i,j)
                print('-')