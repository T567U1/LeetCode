class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        set1 = set(nums)
        for num in set1:
            nums.pop(nums.index(num))
        set2 = set(nums)
        single = int(list(set1 - set2)[0])
        return single
        
        #return 2 * sum(set(nums)) - sum(nums)

nums = [4,1,2,1,2]
c = Solution()
print(c.singleNumber(nums))
