class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return list(set(list(range(len(nums) + 1))) - set(nums))[-1]

nums = [9,6,4,2,3,5,7,0,1]
c =Solution()
print(c.missingNumber())
