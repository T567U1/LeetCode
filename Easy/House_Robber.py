class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        You are a professional robber planning to rob houses along a street.
        Each house has a certain amount of money stashed,
        the only constraint stopping you from
        robbing each of them is that adjacent houses have security system connected
        and it will automatically contact the police if two adjacent houses were
        broken into on the same night.

        Given a list of non-negative integers representing the amount of money
        of each house, determine the maximum amount of money you can rob tonight
        without alerting the police.
        """
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        max_money = 0
        for i in range(2,len(nums)):
            max_money = max(prev2, prev1 + nums[i])
            prev1 = prev2
            prev2 = max_money
        return max_money

nums = [2,1,1,2]
c = Solution()
print(c.rob(nums))
