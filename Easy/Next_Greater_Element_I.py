class Solution:
    def nextGreaterElement(self, nums1, nums2):
        return_list = []
        for i in nums1:
            if i not in nums2:
                return_list.append(-1)
                continue
            #starts at index of i and looks for next biggest num
            for j in nums2[nums2.index(i):]:
                print(return_list, nums2[nums2.index(i):], i, j)
                if j > i:
                    return_list.append(j)
                    j = i
                    break
                #if end of list just adds a -1
                if j == num2[-1]:
                    return_list.append(-1)

        return return_list

num1, num2 = [4,1,2], [1,3,4,2]
c = Solution()
print(c.nextGreaterElement(num1, num2))
