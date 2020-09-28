class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        s = set(haystack)
        s1 = set(needle)
        s3 = s.intersection(s1)
        try:
            s3 = list(s3)[0]
            s4 = haystack.index(s3)
        except:
            return -1

        return s4

haystack = ["hello", "bba"]
cl = Solution()
print(cl.strStr(haystack[0], haystack[1]))
