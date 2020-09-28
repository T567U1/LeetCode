class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
            x = Counter(nums)
            y = Counter(set(nums))
            ans = x - y
            return ans.keys()
