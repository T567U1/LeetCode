class Solution:
    def findMaxConsecutiveOnes(self, nums):
        nums_, sum_ = [], 0
        for i in range(len(nums) + 1):
            if i >= len(nums) or nums[i] == 0:
                nums_.append(sum_)
                sum_ = 0
                continue
            sum_ += nums[i]

        return max(nums_)

nums = [1,1,0,1,1,1]
c =Solution()
print(c.findMaxConsecutiveOnes(nums))
