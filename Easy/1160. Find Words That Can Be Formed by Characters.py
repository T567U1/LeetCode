class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        #you can use default dic here maybe is faster?
        chars = {x: chars.count(x) for x in set(chars)}
        for word in words:
            #check if number of accourances of letter fit the number of occurances of such letter in chars
            for letter in set(word):
                if letter not in chars or word.count(letter) > chars[letter]:
                    break
            #this would only run if loop is completed without break
            else:
                ans.append(len(word))

        return sum(ans) if ans else 0
