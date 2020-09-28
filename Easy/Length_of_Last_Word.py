class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.isspace() or not s:
            return 0
        s = s.strip()
        try:
            last_index = len(s) - s.rindex(" ") - 1
            if last_index == 0:
                last_index += 1
        except:
            last_index = len(s)
        return last_index

w = "    day "
print(len(w))
cl = Solution()
print(cl.lengthOfLastWord(w))
