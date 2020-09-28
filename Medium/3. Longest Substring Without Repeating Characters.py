class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = []
        word = ""
        for i, x in enumerate(s):
            if  x in word:
                ans += len(word),
                word = word[word.index(x) + 1:] + x
            else:
                word += x

        ans += len(word),

        return max(ans)
        
