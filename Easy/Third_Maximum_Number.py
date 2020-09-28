class Solution:
    def thirdMax(self, nums) -> int:
        if not nums: return 0
        #This can be done in one line but time consumption increases
        thrird_max, set_nums = [], list(set(nums))
        if len(set_nums) < 3: return max(nums)
        for i in range(3):
            thrird_max.append(max(set_nums))
            set_nums.remove(max(set_nums))

        return min(thrird_max)


nums = [1, 2, 3, 4]
c = Solution()
print(c.thirdMax(nums))
