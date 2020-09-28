class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        seem = []
        for w in words:
            for i in words:
                if i == w or i in seem:
                    continue
                if i in w:
                    seem.append(i)

        return seem
