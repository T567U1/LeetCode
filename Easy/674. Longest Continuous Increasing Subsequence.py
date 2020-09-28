class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 1
        #don't like this solution.......
        #comeback when motivated haha
        anchor, lens_ = 0, []
        for i in range(len(nums)):
            if i + 1 == len(nums):
                lens_.append(len(nums[anchor: i + 1]))
                break
            if nums[i] >= nums[i + 1]:
                lens_.append(len(nums[anchor: i + 1]))
                anchor = i + 1

        return max(lens_) if lens_ else 0

        #second solution memory used decrease to 95% speed still tank...
        #enumarate may not be the best tool
        class Solution:
            def findLengthOfLCIS(self, nums: List[int]) -> int:
                max_, anchor = 1, 0
                for i, num in enumerate(nums):
                    if num <= nums[i - 1]:
                        max_ = max(len(nums[anchor: i]), max_)
                        anchor = i
                        continue
                    if i + 1 == len(nums):
                        max_ = max(len(nums[anchor:]), max_)

                return max_ if nums else 0

nums = [2, 1]
c = Solution()
print(c.findLengthOfLCIS(nums))
