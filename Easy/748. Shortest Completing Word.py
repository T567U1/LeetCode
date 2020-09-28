class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key = len)
        licensePlate = licensePlate.lower()
        dict_lic = {x.lower(): licensePlate.count(x) for x in licensePlate if x.isalpha()}
        final = ""
        for word in words:
            flag = 1
            for ch in dict_lic:
                if ch in word and dict_lic[ch] <= word.count(ch):
                    continue
                flag = 0
                break

            if flag:
                return word
