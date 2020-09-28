class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #rules to be true:
        #all capitals
        #1 capital follow by lowers
        #or not capitals at all
        if word.isupper() or word.islower() or word.istitle() and word[1:].islower():
            return True
        else:
            return False


c = Solution()
print(c.detectCapitalUse("FFFFFFFFFf"))
