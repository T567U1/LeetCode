class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) > 3:
            ans = ''
            c = 0
            for i in str(n)[::-1]:
                if c == 3:
                    ans += '.'
                    c = 0
                ans += i
                c += 1

            return ans[::-1]
        else:
            return str(n)
