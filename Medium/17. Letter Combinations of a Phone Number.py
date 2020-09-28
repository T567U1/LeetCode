class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
             '2': "abc",
             '3': "def",
             '4': "ghi",
             '5': "jkl",
             '6': 'mno',
             '7' :'pqrs',
             '8': "tuv",
             '9': "wxyz"
            }

        def recurse(dgs):
            if not dgs:
                return []

            elif not dgs[1:]:
                return [v for v in m[dgs[0]]]

            res = []
            for ch1 in m[dgs[0]]:
                for ch2 in recurse(dgs[1:]):
                    res += ch1 + ch2,

            return res

        return recurse(digits)
