class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            for i in range(k):
                nums.insert(0, nums.pop())
        #this line below increases speed by 95% percent memory still high tho
        nums[0:] = nums[-k:] + nums[:-k]


nums = [1,2,3,4,5,6,7]
c = Solution()
print(c.rotate(nums, 3))
