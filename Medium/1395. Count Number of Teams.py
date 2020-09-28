class Solution:
    def numTeams(self, rating: List[int]) -> int:
        r = len(rating)
        res = 0

        for i in range(r):
            for j in range(i + 1, r):
                for k in range(j + 1, r):
                    res += 1 if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k] else 0
        return res
        
