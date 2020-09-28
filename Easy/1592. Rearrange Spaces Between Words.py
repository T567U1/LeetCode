class Solution:
    def reorderSpaces(self, t: str) -> str:
        ans = ''
        t_ = t.split()
        c = t.count(' ')
        w = len(t_) - 1
        if w == 0:
            return t.strip() + ' ' * t.count(' ')
        s = (c // w) if w else 0
        while t_:
            ans = t_.pop() + ' ' * s + ans
            c -= s

        return ans[:c] if c else ans
