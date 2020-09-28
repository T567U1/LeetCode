class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            dic = {}
            seem = {}
            for x, y in zip(word, pattern):
                if y in dic and dic[y] != x:
                    break
                elif y not in dic:
                    if x in seem and seem[x] != y:
                        break
                    dic[y] = x
                    seem[x] = y
            else:
                ans.append(word)

        return ans
