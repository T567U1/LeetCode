class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        S = list(S)
        while i != len(S) - 1:
            if not S:
                break
            if S[i] == S[i + 1]:
                S.pop(i + 1)
                S.pop(i)
                i -= 2 if i != 0 else 1
            i += 1
        return ''.join(S)
