class Solution:
    def findWords(self, words):
        if not words: return []
        return_list = []
        #dictionary of set could be use here to increase speed
        #saw it after but if implemented I feel cheated
        #it works 63% faster
        k_sets = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for word in words:
            s = [i for i in k_sets if word[0].upper() in i]
            #if len(s[0]) == len(set(s[0]) | set(list(word.upper()))):
            #speed was not affected
            if set(word.upper()).issubset(set(s[0])):
                return_list.append(word)

        return return_list

words = ["adsdf","sfd"]
c = Solution()
print(c.findWords(words))
