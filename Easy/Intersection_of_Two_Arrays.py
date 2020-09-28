class Solution:
    def intersection(self, nums1, nums2):
        lr = []
        #pop every single number from num1 and as long number is on both list it will be
        #append to lr which is the one been returned
        while nums1:
            i  = nums1[-1]
            if i in nums1 and i in nums2:
                lr.append(i)
                nums2.remove(i)
            nums1.pop()
        return lr

nums1, nums2 = [1,2,2,1,3], [2, 2, 3]
c = Solution()
print(c.intersection(nums1, nums2))
