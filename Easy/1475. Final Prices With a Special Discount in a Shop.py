class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0] * len(prices)
        for i in range(len(prices)):
            min_ = 0
            for j in prices[i + 1:]:
                if j <= prices[i]:
                    min_ = j
                    break
            ans[i] = prices[i] - min_

        return ans
        
