class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy, sell = prices[0], 0
        for price in prices:
            if price < buy:
                buy = price
            if price - buy > sell:
                sell = price - buy
        return sell
prices = [3,2,6,5,0,3]
c = Solution()
print(c.maxProfit(prices))
