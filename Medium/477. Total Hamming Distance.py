class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit0 = 0
            for i in range(len(nums)):
                if nums[i] & 1:
                    bit0 += 1
                nums[i] >>= 1
            res += bit0 * (len(nums) - bit0)
        return res
