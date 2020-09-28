class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)
        #we have 4 robers in this case and just output the one with the max money
        r, r1 ,l, l1 = nums[1], nums[2], nums[0], nums[1]
        for i in range(2, len(nums) - 1):
            r, l = l + nums[i], max(r, l)
            r1, l1 = l1 + nums[i + 1], max(r1, l1)

        return max(r, r1, l, l1)

n = [1,3,1,3,100]
c = Solution()
print(c.rob(n))
