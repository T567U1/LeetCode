class Solution:
    def minMoves(self, nums) -> int:
        #sum the giving numbers, minus the len of giving numbers * the minimun of numbers
        sum_, len_, min_ =  sum(nums), len(nums), min(nums)
        return sum_ - len_ * min_
