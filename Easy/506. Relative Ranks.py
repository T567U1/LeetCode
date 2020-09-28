class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_t = sorted(nums, reverse = True)
        if len(nums) <= 2:
            if len(nums) == 1:
                return ["Gold Medal"]
            elif len(nums) == 2:
                dic = {
                    nums_t[0]: "Gold Medal",
                    nums_t[1]: "Silver Medal"
                }
                return [dic[i] for i in nums]
        dic = {
            nums_t[0]: "Gold Medal",
            nums_t[1]: "Silver Medal",
            nums_t[2]: "Bronze Medal"
        }
        for i in range(3, len(nums_t)):
            dic[nums_t[i]] = str(i + 1)

        return [dic[i] for i in nums]
        
nums = [5, 4, 3, 2, 1]
c = Solution()
print(c.findRelativeRanks(nums))
