class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                #checks if value stored mach char
                if t[i] == dic[s[i]]:
                    continue
                return 0, dic
                break
            #if key doesn't exist but value does.....
            elif s[i] not in dic and t[i] in dic.values():
                return 0
            else:
                dic[s[i]] = t[i]
        return 1, dic

c = Solution()
print(c.isIsomorphic("ab", "aa"))
