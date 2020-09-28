class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        for i, num in enumerate(nums):
            if num == val:
                nums.pop(i)
        if val in nums:
            for i, num in enumerate(nums):
                if num == val:
                    nums.pop(i)

        return len(nums)
nums = [0,1,2,2,3,0,4,2]
cl = Solution()
print(cl.removeElement(nums, 2))
