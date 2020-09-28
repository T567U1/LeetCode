class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        nums_ = set(nums)
        for i in nums_:
            if i + 1 in nums_:
                dic[i] = nums.count(i) + nums.count(i + 1)

        return max(dic.values()) if dic else 0
