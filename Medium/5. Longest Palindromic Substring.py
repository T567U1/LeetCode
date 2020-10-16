class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                dic[c] += i,
                continue
            dic[c] = [i]
        seen = set()
        ans = ''
        for char, indexs in dic.items():
            for i, x in enumerate(indexs):
                check = indexs[i + 1:]
                while check:
                    a = ''
                    a = s[x:check.pop() + 1]
                    if len(a) > len(ans) and a == a[::-1]:
                        ans = a

        return ans if ans else s[0]
                
