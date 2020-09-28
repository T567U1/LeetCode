class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_t, t_t = [], []
        for i in S:
            if i == '#':
                if s_t:
                    s_t.pop()
                continue
            s_t.append(i)
        for i in T:
            if i == '#':
                if t_t:
                    t_t.pop()
                continue
            t_t.append(i)

        return s_t == t_t
