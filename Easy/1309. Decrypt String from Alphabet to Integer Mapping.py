class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = { str(i) : chr(i + 96) for i in range(1, 27)}
        ans = ''
        for i, x in enumerate(s):
            if x  == '#':
                ans = ans[:-2] + dic[s[i - 2] + s[i - 1]]
                continue
            elif x == '0':
                ans += '0'
                continue
            ans += dic[x]

        return ans
