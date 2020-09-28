class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        for i in t:
            if i in s:
                s.remove(i)
                print(i, s)
            else:
                return False
        return True
        # sorted str s and t must be equals
        #return len(s) == len(t) and sorted(s) == sorted(t)

s, t = "aacc", "ccac"
c = Solution()
print(c.isAnagram(s,t))
