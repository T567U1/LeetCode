class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        counter = 0
        x = str(x)
        middle_out = int(len(x)/2)
        if x[0] == '-':
            return False
        for num in range(len(x), middle_out, -1):
            if x[-len(x) + counter] != x[num - 1]:
                return False
            counter += 1

        return True


cl = Solution()
print(cl.isPalindrome(1321))
