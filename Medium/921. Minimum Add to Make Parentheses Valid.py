class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        open_, close = [], []
        for i in S:
            if i == '(':
                open_.append(i)
            elif i == ')' and open_:
                open_.pop()
            else:
                close.append(i)

        return len(open_) + len(close)
