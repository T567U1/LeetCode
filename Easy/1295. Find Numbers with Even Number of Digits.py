class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for i in nums if len(str(i)) % 2 == 0])
