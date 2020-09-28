class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, count, more_times_on_list = set(nums), 0, 0
        for num in s:
            if nums.count(num) > count:
                count = nums.count(num)
                more_times_on_list = num

        return more_times_on_list

n = [6,5,5]
c = Solution()
print(c.majorityElement(n))
