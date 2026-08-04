class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum_price = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):

            if prices[i] < minimum_price:
                minimum_price = prices[i]

            profit = prices[i] - minimum_price

            maximum_profit = max(maximum_profit, profit)

        return maximum_profit