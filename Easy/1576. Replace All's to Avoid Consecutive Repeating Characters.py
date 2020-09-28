class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s) + ['a']
        c = ['?'] * s.count('?')
        while '?' in s:
            a = (list('abcdefghijklmnopqrstuvwxyz') + c) * 2
            i = s.index('?')
            a.remove(s[i - 1])
            a.remove(s[i + 1])

            s[i] = a[0]

        return ''.join(s[:-1])

                
