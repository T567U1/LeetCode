class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels, s = ['a','e','i','o','u','A','E','I','O','U'], list(s)
        l = [i for i in s[::-1] if i in vowels]
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = l.pop(0)
        return "".join(s)

c = Solution()
print(c.reverseVowels('aA'))
