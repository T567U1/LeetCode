class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans  = []
        for i, num in enumerate(nums):
            ans.append(num)
            for j, x in enumerate(nums[i + 1:]):
                ans.append(x + ans[-1])

        ans.sort()
        return sum(ans[left - 1: right])
