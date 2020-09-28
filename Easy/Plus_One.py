class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = ''.join(str(i) for i in digits)
        digits = list(str(int(digits) + 1))
        return digits


digits = [1,2,3]
cl = Solution()
print(cl.plusOne(digits))
