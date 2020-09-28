class Solution:
    def twoSum(self, numbers, target):
        dic = {}
        #hash table
        for i, x in enumerate(numbers):
            dic[x] = i
        for i, x in enumerate(numbers):
            if target - x in dic:
                return [i + 1, dic.get(target - x) + 1]

c = Solution()
print(c.twoSum([25,50,75], 100))
