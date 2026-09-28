class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices: # 6
            min_price = min(min_price, price) # 1
            max_profit = max(max_profit, price - min_price) # 4, 5
            print(max_profit)

        return max_profit