class Solution:
    def intersect(self, nums1, nums2):
        for i in nums1:
            if i not in nums2:
                nums1.remove(i)
        return nums1
nums1, nums2 = [1,2,2,1], [2]
c = Solution()
print(c.intersect(nums1, nums2))
