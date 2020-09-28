class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # if len of either set or string is off
        if len(set(pattern)) != len(set(str.split())) or len(pattern) != len(str.split()): return False
        # create diccionary
        dic = {pattern[i]: str.split()[i] for i in range(len(pattern))}
        #compare keys to values
        for i in range(len(pattern)):
            print(dic[pattern[i]], str.split()[i])
            if dic[pattern[i]] == str.split()[i]:
                continue
            else: return False
        return True

pattern, str = "aba", "cat cat cat dog"

c = Solution()
print(c.wordPattern(pattern, str))
