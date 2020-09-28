class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            if 1 in nums:
                return sum(nums) - 1
            return 0
        count = carry = 0
        ans = 0
        for num in nums:
            if not num:
                ans = max(ans, carry + count)
                carry = count
                count = 0
            else:
                count += 1
        else:
            ans = max(ans, carry + count)
        return ans
