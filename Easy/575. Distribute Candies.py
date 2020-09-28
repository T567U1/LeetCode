class Solution:
    #the solution as the problem does make sence..... it not about kind of
    #candie each can ghet is about how much each would get.....
    def distributeCandies(self, candies: List[int]) -> int:
        if len(set(candies))>= len(candies) // 2:
            return len(candies) // 2
        else:
            return len(set(candies))
