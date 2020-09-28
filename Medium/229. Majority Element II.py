class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums) // 3
        ans = []
        for i in set(nums):
            if nums.count(i) > k:
                ans += i,
        return ans
