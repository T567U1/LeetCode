class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def go(s):
            s = list(s)
            for i, x in enumerate(s):
                if x is '1':
                    s[i] = '0'
                else:
                    s[i] = '1'

            return '1' + ''.join(s[::-1])

        s = '0'

        while len(s) < k:
            s += go(s)

        return s[k - 1]
