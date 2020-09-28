class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.remove(0)
        for i in nums2:
            nums1.append(i)
        for num in range(len(nums1)-1, 0, -1):
         for index in range(num):
             if nums1[index] > nums1[index + 1]:
                nums1[index], nums1[index + 1] = nums1[index + 1], nums1[index]

        return nums1

nums1, nums2 = [-1,0,1,2,3,0,0,0], [2,5,6]
m, n = 3, 3
c = Solution()
print(c.merge(nums1, m, nums2, n))
