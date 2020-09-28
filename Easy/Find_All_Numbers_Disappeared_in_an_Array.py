class Solution:
    def findDisappearedNumbers(self, nums):
        # first go 7%....
        '''
        if not nums: return []
        len_, max_ = list(range(1, len(nums) + 1)), list(range(1, max(nums)))
        if len(len_) > len(max_): return list(set(len_) - set(nums))
        else: return list(set(max_) - set(nums))
        '''
        #second go 17%...
        '''
        return list(set(list(range(1, len(nums) + 1))) - set(nums))
        '''
        #third go this one decreases to 100% less memory use.... I need an adult
        nums = list(set(range(1, len(nums) + 1)) - set(nums))
        return nums


nums = [1,1]
c = Solution()
print(c.findDisappearedNumbers(nums))
