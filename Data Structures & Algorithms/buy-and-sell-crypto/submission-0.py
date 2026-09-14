class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        chosen = prices[0]
        maxm = 0
        for i in range(len(prices)):
            if prices[i] < chosen:
                maxm = chosen
        print(maxm)