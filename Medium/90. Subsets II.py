class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        ans = {()}
        for x in nums:
            t = ans.copy()
            for y in t:
                a = y[:]
                a += x,
                ans.add(tuple(sorted(list(a))))

        return ans
