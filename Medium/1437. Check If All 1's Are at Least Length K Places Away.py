class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ans = [0]

        for i, x in enumerate(nums):
            if x == 1:
                ans.append(i - ans[-1])
        for i in ans[2:]:
            if i <= k:
                return False

        return True
