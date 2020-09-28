class Solution:
    def sortByBits(self, arr):
        count_ones = {}
        for i in arr:
            count_ones[i] = bin(i)[2:].count('1')

        ans = sorted(count_ones)
        return ans

nums = [1024,512,256,128,64,32,16,8,4,2,1]
c = Solution()
print(c.sortByBits(nums))
