class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        print(enumerate(zip(*strs)))
        for i, letter_group in enumerate(zip(*strs)):
            print(letter_group, i)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
            else:
                return min(strs)

st = [
    ["abab","aba",""],
    ["flower","flow","flight"],
    ["aaa","aa","aaa"],
    ["c","c","c"],
    ["a","b"],
    ["aa","aa"],
    [],
    ["ca","a"],
    [""],
    ["aac","ab"],
    ["aac","acab","aa","abba","aa"]
    ]

cl = Solution()
for array in st:
    print(cl.longestCommonPrefix(array))
    print(">>>>>>>><<<<<<<<")
