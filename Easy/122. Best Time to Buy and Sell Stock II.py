class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in prices[:-1]:
            for x in prices[i:]:
                if i > x:
					break
				else:
					profit += x - i
					i = j
					break
