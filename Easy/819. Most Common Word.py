import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = {}
        str_ = paragraph.translate(paragraph.maketrans(string.punctuation)).upper().split(" ")
        for i in str_:
            if i.lower() in banned:
                continue
            dic[i] = str_.count(i)

        return max(dic, key = dic.get).lower()
