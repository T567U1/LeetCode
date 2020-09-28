class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) == 10:
            return []
        dic = {}
        if len(s) == 10:
            return s
        for i in range(len(s) - 9):
            if s[i: i + 10] in dic:
                dic[s[i: i + 10]] += 1
            else:
                dic[s[i: i + 10]] = 1

        ans = []
        for key in dic:
            if dic[key] > 1:
                ans += key,

        return ans
                
