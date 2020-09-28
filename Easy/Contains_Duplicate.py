class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # true and falls can be avoid
        # return len(set(nums)) != len(nums)
        return False if len(set(nums)) == len(nums) else True


nums = [1,1,4,6,0,0]
c = Solution()
print(c.containsDuplicate(nums))
