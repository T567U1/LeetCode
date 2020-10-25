class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for x, y in zip(l, r):
            temp = sorted(nums[x : y + 1])
            d = abs(temp[0] - temp[1])
            for j, x1 in enumerate(temp[1:]):
                y1 = abs(temp[j] - x1)
                if d != y1:
                    ans += False,
                    break
            else:
                ans += True,

        return ans
